import subprocess
import os
import json

# 设置文件夹路径
# folder_path = 'data/SecurityEval/code'
# folder_path = 'data/SecCodePLT/code'

folder_path = 'data/SecCodePLT/fixed_code_5'
save_path = 'data/SecCodePLT/bandit_SecCodePLT_fixed_5.json'
# 初始化结果存储列表
scan_results = []

# 遍历文件夹中的所有 Python 文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):  # 检查文件扩展名是否为 .py
            file_path = os.path.join(root, file)
            print(f"正在对 {file_path} 进行 Bandit 安全扫描...")

            # 执行 Bandit 测试
            result = subprocess.run(['bandit', '-r', file_path], capture_output=True, text=True)

            # 检查是否有安全问题
            if "No issues identified" not in result.stdout:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_code = f.read()

                # 创建字典并将结果保存
                scan_results.append({
                    "ID": file,
                    "code": file_code,
                    "bandit_result": result.stdout
                })


# 将结果写入 JSON 文件
with open(save_path, 'w', encoding='utf-8') as json_file:
    json.dump(scan_results, json_file, indent=4, ensure_ascii=False)

print(len(scan_results))
print(f"扫描完成，结果已保存到文件中")
