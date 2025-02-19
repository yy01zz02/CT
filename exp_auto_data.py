import json
import os
import requests
import time


def get_text(text):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Pro/deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ],
        "max_tokens": 8192,
    }
    headers = {
        "Authorization": "Bearer sk-iewubqewnuedfxzlkyioxkvbnxnbsuenonbhrjffdbnvgdli",
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




flag = True
while flag:
    file_path = 'data/PromSec/bandit/bandit_PromSec_fixed_6.json'
    save_path = 'data/PromSec/deepseek/deepseek_PromSec_fixed_6.json'

    # 读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    results = []
    error_count = 0
    # 处理每一条数据
    for entry in data:
        try:
            ID = entry['ID']
            code = entry['code']
            bandit_result = entry['bandit_result']
            bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()



            prompt = f"""
            You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.
    
            Vulnerable Code:
            {code}
    
            Bandit Analysis Results:
            {bandit_result}
    
            Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
            """

            content = get_text(prompt)

            result = {
                "ID": ID,
                "content": content
            }

            results.append(result)

            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4)

            print(f"ID {ID} 的结果已保存。")

        except Exception as e:
            error_count += 1
            print(f"处理 ID {entry['ID']} 时发生错误（错误次数: {error_count}）：{e}")
            if error_count >= 100:
                print("错误次数达到100次，程序终止。")
                break



    import re

    file_path = 'data/PromSec/deepseek/deepseek_PromSec_fixed_6.json'
    save_path = 'data/PromSec/reasoning/fixed_and_reason_6.json'

    # 读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 用来保存处理后的数据
    output_data = []

    cnt = 0
    # 遍历 JSON 文件中的所有项，解析 text 字段
    for item in data:
        text = item.get("content")
        if text:
            # 解析 text 字段中的内容
            try:
                parsed_data = json.loads(text)
                content = parsed_data["choices"][0]["message"]["content"]
                reasoning_content = parsed_data["choices"][0]["message"]["reasoning_content"]

                # 打印解析后的内容
                print(f"ID: {item['ID']}")
                print("Fixed_code:")
                print(content)
                print("\nReasoning Content:")
                print(reasoning_content)

                cleaned_content = re.sub(r'```python\n', '', content)  # 去除开头的 ```python\n
                cleaned_content = re.sub(r'```$', '', cleaned_content)  # 去除结尾的 ```

                # 保存到 output_data 列表
                output_data.append({
                    "ID": item['ID'],
                    "Fixed_code": cleaned_content,
                    "reasoning_content": reasoning_content
                })

                cnt += 1
                print("-" * 50, cnt)  # 分隔线

            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing text for ID {item['ID']}: {e}")
        else:
            print(f"Text field is missing for ID {item['ID']}")

    # 将结果保存到一个新的 JSON 文件
    with open(save_path, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, ensure_ascii=False, indent=4)

    print("Data has been written")



    cnt = 0
    def json_to_py(file_path, save_folder):
        # 读取 JSON 文件
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 创建保存 Python 文件的文件夹（如果不存在）
        output_folder = save_folder
        os.makedirs(output_folder, exist_ok=True)
        global cnt
        # 遍历 JSON 数据并将每个 code 写入对应的 Python 文件
        for entry in data:
            cnt += 1
            file_name = f"{entry['ID']}"  # 文件名为 id.py
            file_path = os.path.join(output_folder, file_name)  # 文件保存路径

            with open(file_path, 'w', encoding='utf-8') as py_file:
                py_file.write(entry['Fixed_code'])  # 将代码写入文件

        print(f"所有 Python 文件已成功写入 {output_folder} 文件夹中")


    file_path = 'data/PromSec/reasoning/fixed_and_reason_6.json'
    save_folder = 'data/PromSec/fixed_code_7'

    json_to_py(file_path, save_folder)
    print(cnt)

    import subprocess
    import os
    import json


    folder_path = 'data/PromSec/fixed_code_7'
    save_path = 'data/PromSec/bandit/bandit_PromSec_fixed_7.json'
    # 初始化结果存储列表
    scan_results = []

    # 遍历文件夹中的所有 Python 文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):  # 检查文件扩展名是否为 .py
                file_path = os.path.join(root, file)
                print(f"正在对 {file_path} 进行 Bandit 安全扫描...")

                # 执行 Bandit 测试
                result = subprocess.run(['bandit', '-r', file_path], capture_output=True, text=True)

                # 检查是否有安全问题
                if "No issues identified" not in result.stdout:
                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_code = f.read()

                    # 创建字典并将结果保存
                    scan_results.append({
                        "ID": file,
                        "code": file_code,
                        "bandit_result": result.stdout
                    })



    print(len(scan_results))
    print(f"扫描完成，结果已保存到文件中")

    if len == 0:
        flag = False
        # 将结果写入 JSON 文件
        with open(save_path, 'w', encoding='utf-8') as json_file:
            json.dump(scan_results, json_file, indent=4, ensure_ascii=False)

    else:
        print("失败-------------------------------------------------")
        print("失败-------------------------------------------------")
        print("失败-------------------------------------------------")
        print("失败-------------------------------------------------")
        print("失败-------------------------------------------------")




