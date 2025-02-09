import json


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def count_common_entries(file1, file2):
    """Count the number of common entries between two JSON files."""
    data1 = load_json(file1)
    data2 = load_json(file2)

    if not isinstance(data1, list) or not isinstance(data2, list):
        raise ValueError("Both JSON files should contain lists of data.")

    set1 = {json.dumps(entry, sort_keys=True) for entry in data1}
    set2 = {json.dumps(entry, sort_keys=True) for entry in data2}

    common_entries = set1.intersection(set2)
    return len(common_entries)


# 示例：比较两个 JSON 文件
json_file1 = "data/SecurityEval/fixed_and_reason_all.json"
json_file2 = "data/SecurityEval/fixed_and_reason.json"
common_count = count_common_entries(json_file1, json_file2)
print(f"Number of common entries: {common_count}")
