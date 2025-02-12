import os
import json


# 读取 JSON 文件
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


# 保存 JSON 文件
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


output_path = "data/SecCodePLT/fixed_and_reason_all.json"  # 更新后的 JSON


json1_path = "data/SecCodePLT/fixed_and_reason_3.json"  # 原始包含错误数据的 JSON
json2_path = 'data/SecCodePLT/fixed_and_reason_4.json'  # 包含修正数据的 JSON
json1_data = load_json(json1_path)
json2_data = load_json(json2_path)

# 创建 ID 到修正数据的映射
fix_dict = {entry['ID']: entry for entry in json2_data}

# 替换错误数据
updated_data = []
for entry in json1_data:
    if entry['ID'] in fix_dict:
        updated_data.append(fix_dict[entry['ID']])  # 用正确数据替换
    else:
        updated_data.append(entry)  # 保持原数据



json1_path = "data/SecCodePLT/fixed_and_reason_2.json"  # 原始包含错误数据的 JSON
json1_data = load_json(json1_path)
json2_data = updated_data

# 创建 ID 到修正数据的映射
fix_dict = {entry['ID']: entry for entry in json2_data}

# 替换错误数据
updated_data = []
for entry in json1_data:
    if entry['ID'] in fix_dict:
        updated_data.append(fix_dict[entry['ID']])  # 用正确数据替换
    else:
        updated_data.append(entry)  # 保持原数据


json1_path = "data/SecCodePLT/fixed_and_reason_1.json"  # 原始包含错误数据的 JSON
json1_data = load_json(json1_path)
json2_data = updated_data

# 创建 ID 到修正数据的映射
fix_dict = {entry['ID']: entry for entry in json2_data}

# 替换错误数据
updated_data = []
for entry in json1_data:
    if entry['ID'] in fix_dict:
        updated_data.append(fix_dict[entry['ID']])  # 用正确数据替换
    else:
        updated_data.append(entry)  # 保持原数据


json1_path = "data/SecCodePLT/fixed_and_reason.json"  # 原始包含错误数据的 JSON
json1_data = load_json(json1_path)
json2_data = updated_data

# 创建 ID 到修正数据的映射
fix_dict = {entry['ID']: entry for entry in json2_data}

# 替换错误数据
updated_data = []
for entry in json1_data:
    if entry['ID'] in fix_dict:
        updated_data.append(fix_dict[entry['ID']])  # 用正确数据替换
    else:
        updated_data.append(entry)  # 保持原数据



save_json(output_path, updated_data)


print("数据更新完成，结果已保存到:", output_path)
