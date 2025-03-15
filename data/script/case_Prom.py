import json
import os
import subprocess

import requests
import time
from experimental_methods import reasoning_fix, remove_backticks


def get_text(message):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        # "model": "Pro/deepseek-ai/DeepSeek-R1",
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": message,
        "max_tokens": 8192,
    }
    headers = {
        "Authorization": "Bearer sk-srnuynjinkifiptsxnpfeeaasxljkhusxornyulecijwgbvk",
        "Content-Type": "application/json"
    }

    for attempt in range(100):  # 最多重试100次
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # 检查HTTP错误
            return response.text
        except requests.RequestException as e:
            print(f"请求失败，重试 {attempt + 1}/100: {e}")
            time.sleep(10)  # 休眠5秒后重试

    raise Exception("连续100次请求失败，程序终止。")


# names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]
# for name in names:


name = "PromSec"

file_path = f'{name}/block_{name}.json'
save_path = f'{name}/fixed_{name}.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

results = []
error_count = 0

if os.path.exists(save_path):
    with open(save_path, 'r', encoding='utf-8') as ff:
        try:
            results = json.load(ff)
        except json.JSONDecodeError:
            results = []
else:
    results = []

# 处理每一条数据
for entry in data:
    try:
        id = entry['id']

        if any(temp_result['id'] == id for temp_result in results):
            continue

        bug = entry['bug']
        bug_before = entry['bug_before']
        bug_after = entry['bug_after']
        issue = entry['issue']

        cnt = 0

        messages = [
            {"role": "system", "content": "You are a code vulnerability expert. Below is a vulnerable code "
                                          "snippet along with the results from vulnerability analysis tools. "
                                          "Your task is to fix the vulnerabilities and provide the "
                                          "corrected version of the code."}
        ]

        br = ""
        while cnt < 5:
            cnt += 1
            if cnt == 1:
                prompt = reasoning_fix(bug, bug_before, bug_after, issue)
            else:
                prompt = (f"Your previous response was not accepted. Please try again.\n"
                          f"The vulnerability analysis is as follows:\n{br}")

            messages.append({"role": "user", "content": prompt})

            print(prompt)
            print()

            text = get_text(messages)
            parsed_data = json.loads(text)
            fix_code = parsed_data["choices"][0]["message"]["content"]
            cot = parsed_data["choices"][0]["message"]["reasoning_content"]

            messages.append({"role": "assistant", "content": fix_code})

            fix_code_file = remove_backticks(fix_code)

            print(fix_code_file)
            print()

            with open(f'{id}.py', "w") as f:
                f.write(fix_code_file)

            print(f"正在对 f'{id}.py' 进行 Bandit 安全扫描..., 第 {cnt} 次")

            # 执行 Bandit 测试
            bandit_run = subprocess.run(
                ['bandit', '-r', f'{id}.py'],
                capture_output=True, text=True)

            if os.path.exists(f'{id}.py'):
                os.remove(f'{id}.py')

            if "No issues identified" in bandit_run.stdout:
                break

            br = bandit_run.stdout.split('Test results:')[1].split('Code scanned:')[0].strip()

        result = {
            "id": id,
            "fix_code": fix_code,
            "cot": cot,
            "count": cnt
        }

        if cnt == 5:
            continue

        results.append(result)

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"ID {id} 的结果已保存。")

    except Exception as e:
        error_count += 1
        print(f"处理 ID {entry['id']} 时发生错误（错误次数: {error_count}）：{e}")
        if error_count >= 100:
            print("错误次数达到100次，程序终止。")
            break
