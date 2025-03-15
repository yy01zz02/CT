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

    # 遍历所有数据，统计 flag = 1 和 flag = 0 的数量
    for item in data:
        if item.get('flag') == '1' :
            count_1 += 1
        elif item.get('flag') == '0':
            count_0 += 1

    total = count_1 + count_0

    if total == 0:
        ratio = 0  # 避免除以零
    else:
        ratio = count_1 / total  # 计算1的比例

    print(filename)
    print(f"flag=1的数量: {count_1}")
    print(f"flag=0的数量: {count_0}")
    print(f"flag=1的比例: {ratio:.2f}")
    print('---------------------------------')


model_name = "deepseek-coder-7b-instruct-v1.5"
# model_name = "Qwen2.5-Coder-7B-Instruct"
data_names = ['SecurityEval', 'CyberSecEval', 'PromSec', 'SecCodePLT']

for name in data_names:
    filename = f'C:/Users/26979/Desktop/exp/exp/{model_name}/{name}/prompt_cot.json'
    calculate_flag_ratio(filename)
    filename = f'C:/Users/26979/Desktop/exp/exp2/{model_name}/{name}/prompt_not_cot.json'
    calculate_flag_ratio(filename)
    filename = f'C:/Users/26979/Desktop/exp/exp/{model_name}/{name}/prompt_cot_nosx.json'
    calculate_flag_ratio(filename)
    filename = f'C:/Users/26979/Desktop/exp/exp2/{model_name}/{name}/prompt_not_cot_not_sx.json'
    calculate_flag_ratio(filename)
