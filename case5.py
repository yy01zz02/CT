import subprocess
import os

# 设置文件夹路径和目标 Python 文件
folder_path = 'data/SecCodePLT/'  # 你想要扫描的文件夹
file_name = '0a0b19a7.py'  # 你想要扫描的 Python 文件名

# 构建完整的文件路径
file_path = os.path.join(folder_path, file_name)

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"文件 {file_path} 不存在！")
else:
    # 执行 Bandit 测试
    print(f"正在对 {file_path} 进行 Bandit 安全扫描...")
    result = subprocess.run(['bandit', '-r', file_path], capture_output=True, text=True)

    # 打印 Bandit 输出
    print("Bandit 扫描结果:")
    print(result.stdout)

    if result.stderr:
        print("错误信息:")
        print(result.stderr)

