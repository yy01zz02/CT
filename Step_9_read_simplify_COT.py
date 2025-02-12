import json
import re

file_path = 'data/PromSec/PromSec_data_simplify.json'
save_path = 'data/PromSec/PromSec_final.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 用来保存处理后的数据
output_data = []

cnt = 0
# 遍历 JSON 文件中的所有项，解析 text 字段
for item in data:
    text = item.get('simplify_cot', '')
    if text:
        try:
            parsed_data = json.loads(text)
            simplify_content = parsed_data['choices'][0]['message']['content']

            # 将 s_content 字段添加到原始数据中
            item['s_cot'] = simplify_content

            output_data.append(item)

            cnt += 1


        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing text for ID {item.get('ID', 'Unknown ID')}: {e}")
    else:
        print(f"Text field is missing for ID {item.get('ID', 'Unknown ID')}")

# 将结果保存到一个新的 JSON 文件
with open(save_path, 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("Data has been written")
