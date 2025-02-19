import json

# 读取json文件
with open('data/SecCodePLT/SecCodePLT_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(len(data))
# 过滤掉"fixed_code"为空字符串的条目
filtered_data = [entry for entry in data if entry.get('fixed_code') != ""]
print(len(filtered_data))

# 将过滤后的数据写回到json文件
with open('data/SecCodePLT/SecCodePLT_data.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4)

print("处理完成，已删除'fixed_code'为空字符串的条目。")
