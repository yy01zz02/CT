import os

import json

from experimental_methods import reasoning_fix, remove_backticks

device = "cuda"
model_list = ["/home/zdx_zp/model/Qwen/Qwen2.5-Coder-7B-Instruct",
              "/home/zdx_zp/model/deepseek-ai/deepseek-coder-7b-instruct-v1.5",
              "/home/zdx_zp/model/AI-ModelScope/codegemma-7b-it"]

vers = "2"


for model_path in model_list:

    messages = []

    model_name = model_path.split('/')[-1]

    data_names = ['CyberSecEval', 'PromSec', 'SecCodePLT', 'SecurityEval']
    for name in data_names:

        # 漏洞数据集
        with open(f'../{name}/{name}_cot_{vers}.json', 'r', encoding='utf-8') as file_b:
            data = json.load(file_b)



        for item in data:
            id = item.get('id')

            if id != "SecurityEval_45":
                continue

            bug = item.get('bug')
            bug_before = item.get('bug_before')
            bug_after = item.get('bug_after')
            issue = item.get('issue')

            prompt = reasoning_fix(bug, issue, bug_before, bug_after)

            pre = "You are a code vulnerability expert.\n"

            prompt = pre + prompt

            print(prompt)
            break
