import json
import re


file_path = 'data/SecCodePLT/deepseek_SecCodePLT_fixed_4.json'
save_path = 'data/SecCodePLT/fixed_and_reason_4.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 用来保存处理后的数据
output_data = []

cnt = 0
# 遍历 JSON 文件中的所有项，解析 text 字段
for item in data:
    text = item.get("content")
    if text:
        # 解析 text 字段中的内容
        try:
            parsed_data = json.loads(text)
            content = parsed_data["choices"][0]["message"]["content"]
            reasoning_content = parsed_data["choices"][0]["message"]["reasoning_content"]

            # 打印解析后的内容
            print(f"ID: {item['ID']}")
            print("Fixed_code:")
            print(content)
            print("\nReasoning Content:")
            print(reasoning_content)

            cleaned_content = re.sub(r'```python\n', '', content)  # 去除开头的 ```python\n
            cleaned_content = re.sub(r'```$', '', cleaned_content)  # 去除结尾的 ```

            # 保存到 output_data 列表
            output_data.append({
                "ID": item['ID'],
                "Fixed_code": cleaned_content,
                "reasoning_content": reasoning_content
            })

            cnt += 1
            print("-" * 50, cnt)  # 分隔线

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing text for ID {item['ID']}: {e}")
    else:
        print(f"Text field is missing for ID {item['ID']}")

# 将结果保存到一个新的 JSON 文件
with open(save_path, 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("Data has been written")
