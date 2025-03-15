import matplotlib

matplotlib.use('TkAgg')  # 选择一个兼容的后端

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置全局字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据集统计信息
datasets = {
    "SecurityEval": {
        "20": 10,
        "22": 1,
        "78": 8,
        "89": 3,
        "94": 2,
        "259": 8,
        "295": 1,
        "319": 2,
        "326": 2,
        "327": 8,
        "330": 2,
        "377": 4,
        "400": 2,
        "502": 5,
        "605": 1,
        "703": 1,
        "732": 1,
        "Total": 61
    },
    "CyberSecEval": {
        "78": 47,
        "259": 8,
        "327": 5,
        "330": 10,
        "377": 1,
        "400": 1,
        "502": 13,
        "703": 14,
        "Total": 99
    },
    "PromSec": {
        "20": 40,
        "22": 7,
        "78": 67,
        "89": 384,
        "259": 48,
        "327": 10,
        "377": 2,
        "400": 5,
        "703": 4,
        "Total": 567
    },
    "SecCodePLT": {
        "20": 18,
        "78": 109,
        "330": 33,
        "400": 1,
        "502": 74,
        "703": 1,
        "Total": 236
    }
}

# 设置 Seaborn 样式
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.2)

# 创建 2x2 子图布局
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

# 画图
for i, (dataset_name, data) in enumerate(datasets.items()):
    # 去掉总计值，只留下 CWE 数据
    cwe_counts = {cwe: count for cwe, count in data.items() if cwe != "Total"}
    cwe_labels = list(cwe_counts.keys())
    cwe_values = list(cwe_counts.values())

    # 创建一个 DataFrame，用于更方便的处理
    df = pd.DataFrame({
        'CWE': cwe_labels,
        'Count': cwe_values
    })

    # 排序以便展示
    df = df.sort_values(by="Count", ascending=False)

    # 绘制条形图
    sns.barplot(x="Count", y="CWE", data=df, ax=axes[i], hue="CWE", palette="viridis", legend=False)

    # 设置标题
    axes[i].set_title(f"{dataset_name}", fontsize=16, fontweight='bold')
    axes[i].set_xlabel("Count", fontsize=14, fontweight='bold')
    axes[i].set_ylabel("CWE-ID", fontsize=14, fontweight='bold')

    # 添加数据标签
    for index, value in enumerate(df['Count']):
        axes[i].text(value, index, str(value), va='center', ha='left', fontsize=12, fontweight='bold',
                     color='black')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()