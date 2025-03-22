import requests
import json

url = 'http://localhost:11434/api/chat'
headers = {
    'Content-Type': 'application/json'
}
data = {
    # 'model': 'llama3.1:8b',
    'model': 'qwen2.5-coder-3b-gguf',
    'messages': [
        {'role': 'user', 'content': 'hello'}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

texts = response.text
texts = texts.split('\n')
texts = [json.loads(text) for text in texts if text]
print(response.status_code)
print(type(texts))
for text in texts:
    print(text['message']['content'], end='')
