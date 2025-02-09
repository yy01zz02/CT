import json

def filter_python_language(json_file1, json_file2, output_file):
    # 读取第一个JSON文件
    with open(json_file1, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)

    # 读取第二个JSON文件
    with open(json_file2, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)

    # 合并两个数据
    combined_data = data1 + data2


    # 映射新的键名
    key_mapping = {
        'file_path': 'ID',
        'origin_code': 'code'
    }

    # 筛选出language为'python'的数据，并修改字段名
    python_data = []
    cnt = 1
    for i, item in enumerate(combined_data):
        if item.get('language') == 'python':
            modified_item = {}
            for key in ('file_path', 'origin_code'):
                if key == 'file_path':
                    modified_item[key_mapping.get(key, key)] = f"CyberSecEval_{cnt}.py"
                    cnt += 1
                else:
                    modified_item[key_mapping.get(key, key)] = item.get(key)
            python_data.append(modified_item)

    # 写入新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(python_data, output, ensure_ascii=False, indent=4)

# 使用示例
filter_python_language('autocomplete.json', 'instruct.json', 'CyberSecEval.json')
