import requests
import re

# 目标网页URL
url = 'https://stackoverflow.com/questions?tab=votes&page=1'

# 发起GET请求获取网页内容
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    # print(html_content)
else:
    print(f"请求失败，状态码：{response.status_code}")
    exit()

# 定义正则表达式，匹配类似于 https://stackoverflow.com/questions/ 开头的网址
pattern = r'/questions/\d+/[\w-]+'

# 使用正则表达式查找所有匹配的网址
urls = re.findall(pattern, html_content)

# 输出所有匹配的链接
for link in urls:
    print(link)
