import ollama

model_name = "qwen2.5-coder-3b-gguf"

response = ollama.generate(
    model=model_name,
    prompt="Hello! How are you?",
    stream=False  # 防止 stream 卡住
)

print(response['response'])
