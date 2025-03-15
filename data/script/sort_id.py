import json


def sort_json_by_id_number(input_file, output_file):
    # 读取JSON文件
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取'id'字段后面的数字并进行排序
    sorted_data = sorted(data, key=lambda x: int(x['id'].split('_')[1]))

    # 将排序后的数据写入新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, ensure_ascii=False, indent=4)


name = "SecCodePLT"

# 输入文件路径和输出文件路径
input_file = f'{name}/fixed_{name}.json'  # 请替换为实际的文件路径
output_file = f'{name}/fixed_sorted_{name}.json'  # 输出文件路径

sort_json_by_id_number(input_file, output_file)
