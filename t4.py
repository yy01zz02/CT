import json
import os


# 读取 JSON 文件并统计 flag 字段的值
def calculate_flag_ratio(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Skipping...")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count_1 = 0
    count_0 = 0

    res = []
    idx = 0
    # 遍历所有数据，统计 flag = 1 和 flag = 0 的数量
    for item in data:
        # if item.get('flag') == '1' and item.get('fix_count') == 1:
        if item.get('flag') == '1':
            count_1 += 1
            res.append(idx)
        elif item.get('flag') == '0':
            count_0 += 1

        idx += 1

    total = count_1 + count_0

    if total == 0:
        ratio = 0  # 避免除以零
    else:
        ratio = count_1 / total  # 计算1的比例


    print(f"flag=1的数量: {count_1}, flag=0的数量: {count_0}, flag=1的比例: {ratio:.2f}")

    return res

def calculate_flag_ratio_1(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Skipping...")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count_1 = 0
    count_0 = 0

    res = []
    idx = 0
    # 遍历所有数据，统计 flag = 1 和 flag = 0 的数量
    for item in data:
        if item.get('flag') == '1' and item.get('fix_count') == 1:
        # if item.get('flag') == '1':
            count_1 += 1
            res.append(idx)
        elif item.get('flag') == '0':
            count_0 += 1

        idx += 1

    total = count_1 + count_0

    if total == 0:
        ratio = 0  # 避免除以零
    else:
        ratio = count_1 / total  # 计算1的比例


    print(f"flag=1的数量: {count_1}, flag=0的数量: {count_0}, flag=1的比例: {ratio:.2f}")

    return res



model_names = ["Qwen2.5-Coder-7B-Instruct", "deepseek-coder-7b-instruct-v1.5", "codegemma-7b-it"]
# model_names = ["Qwen2.5-Coder-32B-Instruct-GPTQ-Int4"]
data_names = ['SecurityEval', 'CyberSecEval', 'PromSec', 'SecCodePLT']


file_1 = "C:/Users/26979/Desktop/exp"
# file_1 = "C:/Users/26979/WPSDrive/830490401/WPS云盘/毕业设计/总结资料/exp_2"

for model_name in model_names:
    for name in data_names:
        for i in range(3):
            print(f'{i}--------{model_name}-----------{name}')
            print('normal: ', end=' ')
            filename = f'{file_1}/{i}/{model_name}/{name}/normal.json'
            lst1 = calculate_flag_ratio(filename)
            print('normal_mul: ', end=' ')
            filename = f'{file_1}/{i}/{model_name}/{name}/normal.json'
            lst1_1 = calculate_flag_ratio_1(filename)
            print('oneshot: ', end=' ')
            filename = f'{file_1}/{i}/{model_name}/{name}/oneshot.json'
            lst2 = calculate_flag_ratio(filename)
            print('COT_2: ', end=' ')
            filename = f'{file_1}/{i}/{model_name}/{name}/cot_2.json'
            lst3 = calculate_flag_ratio(filename)
            print('COT_Step: ', end=' ')
            filename = f'{file_1}/{i}/{model_name}/{name}/cot_step.json'
            lst4 = calculate_flag_ratio(filename)

            # 计算lst2不在lst1中的数量
            count_lst2_not_in_lst1 = len([item for item in lst2 if item not in lst1])
            print([item for item in lst2 if item not in lst1])

            # 计算lst3不在lst1中的数量
            count_lst3_not_in_lst1 = len([item for item in lst3 if item not in lst1])
            print([item for item in lst3 if item not in lst1])

            # 计算lst4不在lst1中的数量
            count_lst4_not_in_lst1 = len([item for item in lst4 if item not in lst1])
            print([item for item in lst4 if item not in lst1])

            # 计算lst3不在lst1和lst2中的数量
            count_lst3_not_in_lst1_and_lst2 = len([item for item in lst3 if item not in lst1 and item not in lst2])
            print([item for item in lst3 if item not in lst1 and item not in lst2])


            # 计算lst4不在lst1和lst2中的数量
            count_lst4_not_in_lst1_and_lst2 = len([item for item in lst4 if item not in lst1 and item not in lst2])
            print([item for item in lst4 if item not in lst1 and item not in lst2])


            print(f"oneshot多修复的数量: {count_lst2_not_in_lst1}")
            print(f"COT_2多修复的数量: {count_lst3_not_in_lst1}")
            print(f"COT_Step多修复的数量: {count_lst4_not_in_lst1}")
            print()
            print(f"COT_2多修复oneshot的数量: {count_lst3_not_in_lst1_and_lst2 }")
            print(f"COT_Step多修复oneshot的数量: {count_lst4_not_in_lst1_and_lst2}")

            print('---------------------------------')
