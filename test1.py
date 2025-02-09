import json
from openai import OpenAI
client = OpenAI(api_key="", base_url="https://api.deepseek.com")

file_path = 'data/SecurityEval/bandit/bandit_SecurityEval.json'

save_path = 'data/SecurityEval/fixed_SecurityEval_deepseek_sample.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 遍历 JSON 数据并生成 LLM 提示语
for entry in data:
    code = entry['code']
    bandit_result = entry['bandit_result']

    bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()
    # 拼接生成的提示语
    prompt = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable Code:
{code}

Bandit Analysis Results:
{bandit_result}

Please provide the fixed version of the code. You only need to give me the corrected code, no additional steps are necessary!!!
    """

    # 输出生成的提示语
    print(prompt)

    client = OpenAI(api_key="sk-3ee8a192db1b4ad6a7ce793d0fd09d18", base_url="https://api.deepseek.com")
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages
    )

    reasoning_content = response.choices[0].message.reasoning_content
    content = response.choices[0].message.content

    print(reasoning_content)
    print(content)

    result = {
        "ID": entry['ID'],
        "reasoning_content": reasoning_content,
        "content": content
    }

    # 每次保存数据
    with open(save_path, 'a', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
        f.write('\n')  # 每条数据单独一行

print("所有结果已保存到 'fixed_code_results.json' 文件中")

