import json
from datasets import load_dataset

# 加载数据集
ds = load_dataset("Virtue-AI-HUB/SecCodePLT")

# 打开输出的 JSON 文件
with open('SecCodePLT_1.json', 'w', encoding='utf-8') as f:
    output_data = []

    # 遍历每一行数据
    for entry in ds["insecure_coding"]:
        # 获取 ID
        id = entry["id"]

        # install_requires = entry["install_requires"]

        # begin = ''

        # for i in install_requires:
        #     if i == 'numpy':
        #         begin += f'import {i} as np\n'
        #     else:
        #         begin += f'import {i}\n'

        # 获取 task_description 中的 description
        comment = entry["task_description"]['description']

        # 获取 ground_truth 中的 vulnerable_code
        code = entry["ground_truth"]

        # 合成完整的 code
        code_combined = f'"""\n{comment}\n"""' + code['code_before'] + code['vulnerable_code'] + code['code_after']

        # 将 id 和 code 保存到字典中
        output_data.append({"id": id, "code": code_combined})

    # 写入 JSON 文件
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print("数据已成功写入 output.json 文件")
