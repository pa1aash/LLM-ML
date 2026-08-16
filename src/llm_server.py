#!/usr/bin/env python3
"""
Simple local LLM server using transformers. 
OpenAI-compatible /v1/chat/completions endpoint.
Uses Qwen3-8B on the GH200.
"""

import json
import sys
import torch
from http.server import HTTPServer, BaseHTTPRequestHandler
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "Qwen/Qwen3-8B"
PORT = 8000

print(f"Loading {MODEL_NAME}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
    trust_remote_code=True,
)
model.eval()
print(f"Model loaded. VRAM used: {torch.cuda.memory_allocated(0) / 1e9:.1f} GB")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/v1/chat/completions":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))

        messages = body.get("messages", [])
        temperature = body.get("temperature", 0.7)
        max_tokens = body.get("max_tokens", 2048)

        # Apply chat template
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,  # Disable thinking for faster/cleaner output
        )
        inputs = tokenizer(text, return_tensors="pt").to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=max(temperature, 0.01),
                do_sample=temperature > 0,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id,
            )

        # Decode only the new tokens
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        response_text = tokenizer.decode(new_tokens, skip_special_tokens=True)

        result = {
            "choices": [{
                "message": {"role": "assistant", "content": response_text},
                "finish_reason": "stop",
            }],
            "model": MODEL_NAME,
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def do_GET(self):
        if self.path == "/v1/models":
            result = {"data": [{"id": MODEL_NAME, "object": "model"}]}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        elif self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        sys.stderr.write(f"[LLM] {args[0]}\n")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"LLM server running on port {PORT}")
    sys.stdout.flush()
    server.serve_forever()
