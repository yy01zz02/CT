import json


def count_json_entries(filename):
    """Count the number of entries in a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return len(data) if isinstance(data, list) else 1


# 示例：读取 JSON 文件并计算条目数
json_file = "data/SecCodePLT/reasoning/fixed_and_reason.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")

json_file = "data/SecCodePLT/reasoning/fixed_and_reason_1.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")

json_file = "data/SecCodePLT/reasoning/fixed_and_reason_2.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")

json_file = "data/SecCodePLT/reasoning/fixed_and_reason_3.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")

json_file = "data/SecCodePLT/reasoning/fixed_and_reason_4.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")

json_file = "data/SecCodePLT/reasoning/fixed_and_reason_all.json"
entry_count = count_json_entries(json_file)
print(f"{json_file}: {entry_count}")


