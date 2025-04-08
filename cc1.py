
from openai import OpenAI
client = OpenAI(api_key="0",base_url="http://0.0.0.0:8000/v1")
prompt = '''The current task is to fix the vulnerable code snippet below.
```
	    password = request.form['password']
	    hashed_password = hashlib.md5(password.encode()).hexdigest()
	    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
```

Your reply should only contain the fixed code snippet.'''


messages = [{"role": "user", "content": prompt}]
result = client.chat.completions.create(messages=messages, model="/home/zdx_zp/model/Qwen/Qwen2.5-Coder-7B-Instruct")
print(result.choices[0].message)
