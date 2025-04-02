import json
import os


def calculate_flag_ratio(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Skipping...")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count_1 = 0
    count_0 = 0
    # print(len(data))
    res = []
    idx = 0
    # 遍历所有数据，统计 flag = 1 和 flag = 0 的数量
    for item in data:
        if item.get('flag') == '1':
        # if item.get('flag') == '1':
            count_1 += 1

        elif item.get('flag') == '0':
            count_0 += 1
            res.append(idx)

        idx += 1

    total = count_1 + count_0

    if total == 0:
        ratio = 0  # 避免除以零
    else:
        ratio = count_0 / total  # 计算1的比例


    print(f"flag=1的数量: {count_1}, flag=0的数量: {count_0}, flag=0的比例: {ratio:.2f}")

    return res, count_0



model_names = ["Qwen2.5-Coder-7B-Instruct", "deepseek-coder-7b-instruct-v1.5", "codegemma-7b-it"]
# model_names = ["Qwen2.5-Coder-7B-Instruct", "codegemma-7b-it"]
# model_names = ["Qwen2.5-Coder-32B-Instruct-GPTQ-Int4"]
data_names = ['CyberSecEval', 'PromSec', 'SecCodePLT', 'SecurityEval']


# file_1 = "C:/Users/26979/Desktop/res/exp_original"
# file_1 = "C:/Users/26979/WPSDrive/830490401/WPS云盘/毕业设计/总结资料/exp_2"
file_1 = "C:/Users/26979/Desktop/res/exp_format_not_info"

for model_name in model_names:
    for name in data_names:

        print(f'--------{model_name}-----------{name}')



        print('normal: ', end=' ')
        filename = f'{file_1}/{model_name}/{name}/normal.json'
        lst1, c1 = calculate_flag_ratio(filename)
        print('oneshot: ', end=' ')
        filename = f'{file_1}/{model_name}/{name}/oneshot.json'
        lst2, c2 = calculate_flag_ratio(filename)
        print('COT_2: ', end=' ')
        filename = f'{file_1}/{model_name}/{name}/cot_2.json'
        lst3, c3 = calculate_flag_ratio(filename)
        # print('COT_Step: ', end=' ')
        # filename = f'{file_1}/{model_name}/{name}/cot_step.json'
        # lst4, c4 = calculate_flag_ratio(filename)

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        tot = len(data)

        # 计算lst2不在lst1中的数量
        count_lst2_not_in_lst1 = len([item for item in lst2 if item not in lst1])
        print([item for item in lst2 if item not in lst1])


        # # 计算lst3不在lst1中的数量
        # count_lst3_not_in_lst1 = len([item for item in lst3 if item not in lst1])
        # print([item for item in lst3 if item not in lst1])

        # # 计算lst4不在lst1中的数量
        # count_lst4_not_in_lst1 = len([item for item in lst4 if item not in lst1])
        # print([item for item in lst4 if item not in lst1])

        count_lst3_not_in_lst1_lst2 = len([item for item in lst3 if item not in lst1 and item not in lst2])
        print([item for item in lst3 if item not in lst1 and item not in lst2])

        # count_lst4_not_in_lst1_lst2 = len([item for item in lst4 if item not in lst1 and item not in lst2])
        # print([item for item in lst4 if item not in lst1 and item not in lst2])




        # print(f"oneshot多修复的数量: {count_lst2_not_in_lst1}")
        # print(f"COT_2多修复的数量: {count_lst3_not_in_lst1}")
        # print(f"COT_Step多修复的数量: {count_lst4_not_in_lst1}")
        # print(f"COT_2多oneshot修复的数量: {count_lst3_not_in_lst1_lst2}")
        # print(f"COT_Step多oneshot修复的数量: {count_lst4_not_in_lst1_lst2}")

        c2, c3 = count_lst2_not_in_lst1, count_lst3_not_in_lst1_lst2
        print(f'normal: {c1}, correct: {c1 / tot:.4f}')
        print(f'oneshot: {c1 + c2}, correct: {(c1 + c2) / tot:.4f}')
        print(f'COT: {c1 + c2 + c3}, correct: {(c1 + c2 + c3) / tot:.4f}')
        print('---------------------------------')
