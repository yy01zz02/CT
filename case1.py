import json


# 读取JSON文件
with open('data/SecCodePLT/SecCodePLT_final.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for entry in data:
    buggy_code = entry['buggy_code']
    bandit_result = entry['bandit_result']
    fixed_code = entry['fixed_code']
    reasoning_content = entry['reasoning_content']
    cwe_list = entry['cwe_list']
    simplify_cot = entry['simplify_cot']

    prompt_no_cot = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable Code:
{buggy_code}

Bandit Analysis Results:
{bandit_result}

Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
"""

    print(prompt_no_cot)
    break