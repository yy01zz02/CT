import os

import json

from experimental_methods import cot_prompt, oneshot_prompt

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
            meta_data = item.get('meta_data')
            exp_bug = item.get('exp_bug')

            s_cot = meta_data['s_cot']

            fixed_code = meta_data['fixed_code']

            prompt = cot_prompt(bug, issue, s_cot, exp_bug, fixed_code)
            # prompt = oneshot_prompt(bug, issue, exp_bug, fixed_code, bug_before, bug_after)


            print(prompt)
            break
