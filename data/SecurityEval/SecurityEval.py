import json
from datasets import load_dataset

# 加载数据集
ds = load_dataset("s2e-lab/SecurityEval")

# 打开输出的 JSON 文件，指定 UTF-8 编码
with open('output_security_eval.json', 'w', encoding='utf-8') as f:
    output_data = []

    # 遍历每一行数据
    for entry in ds["train"]:
        # 获取 ID 并去掉最后的 3 个字符
        id = entry["ID"][:-3]

        # 获取 Insecure_code
        insecure_code = entry["Insecure_code"]

        # 将 id 和 insecure_code 保存到字典中
        output_data.append({"id": id, "code": insecure_code})

    # 写入 JSON 文件，确保使用 UTF-8 编码
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print("数据已成功写入 output_security_eval.json 文件")
