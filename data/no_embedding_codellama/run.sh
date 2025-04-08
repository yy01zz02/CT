#!/bin/bash

# 切换到脚本所在目录（可选，根据实际情况来）
# cd "$(dirname "$0")"

# 依次执行脚本，并输出状态信息
python linux_cot.py
echo "linux_cot.py finished running!"

python linux_cot_fix.py
echo "linux_cot_fix.py finished running!"

python linux_few_0.py
echo "linux_few_0.py finished running!"

python linux_few_2.py
echo "linux_few_2.py finished running!"

python linux_few_3.py
echo "linux_few_3.py finished running!"

python linux_few_4.py
echo "linux_few_4.py finished running!"

python linux_few_5.py
echo "linux_few_5.py finished running!"

# 所有脚本运行完成后打印提示信息
echo "All scripts finished running!"
