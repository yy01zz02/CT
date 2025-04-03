import os

import json

from experimental_methods import cot_prompt, oneshot_prompt, oneshot_prompt_5

device = "cuda"
model_list = ["/home/zdx_zp/model/Qwen/Qwen2.5-Coder-7B-Instruct",
              "/home/zdx_zp/model/deepseek-ai/deepseek-coder-7b-instruct-v1.5",
              "/home/zdx_zp/model/AI-ModelScope/codegemma-7b-it"]

vers = "2_few_5"


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

            # bug = item.get('bug')
            # bug_before = item.get('bug_before')
            # bug_after = item.get('bug_after')
            # issue = item.get('issue')
            # meta_data_0 = item.get('meta_data_0')
            # exp_bug_0 = item.get('exp_bug_0')
            # fixed_code_0 = meta_data_0['fixed_code']
            #
            # meta_data_1 = item.get('meta_data_1')
            # exp_bug_1 = item.get('exp_bug_1')
            # fixed_code_1 = meta_data_1['fixed_code']
            #
            # meta_data_2 = item.get('meta_data_2')
            # exp_bug_2 = item.get('exp_bug_2')
            # fixed_code_2 = meta_data_2['fixed_code']
            #
            # prompt = oneshot_prompt(bug, exp_bug_0, fixed_code_0, exp_bug_1, fixed_code_1, exp_bug_2, fixed_code_2)
            # print(prompt)

            print('----------------------------')
            bug = item.get('bug')
            bug_before = item.get('bug_before')
            bug_after = item.get('bug_after')
            issue = item.get('issue')
            meta_data_0 = item.get('meta_data_0')
            exp_bug_0 = item.get('exp_bug_0')
            fixed_code_0 = meta_data_0['fixed_code']

            meta_data_1 = item.get('meta_data_1')
            exp_bug_1 = item.get('exp_bug_1')
            fixed_code_1 = meta_data_1['fixed_code']

            meta_data_2 = item.get('meta_data_2')
            exp_bug_2 = item.get('exp_bug_2')
            fixed_code_2 = meta_data_2['fixed_code']

            meta_data_3 = item.get('meta_data_3')
            exp_bug_3 = item.get('exp_bug_3')
            fixed_code_3 = meta_data_3['fixed_code']

            meta_data_4 = item.get('meta_data_4')
            exp_bug_4 = item.get('exp_bug_4')
            fixed_code_4 = meta_data_2['fixed_code']

            prompt = oneshot_prompt_5(bug, exp_bug_0, fixed_code_0, exp_bug_1, fixed_code_1, exp_bug_2, fixed_code_2,
                                      exp_bug_3, fixed_code_3, exp_bug_4, fixed_code_4)


            print(prompt)
            break
