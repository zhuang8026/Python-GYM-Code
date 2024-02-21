import requests
from bs4 import BeautifulSoup

# 定义要爬取的网页URL
url = 'https://example.com'

# 发送HTTP请求，获取网页内容
response = requests.get(url)
print(response)
# 使用Beautiful Soup解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取标题和链接
title = soup.title.text
links = soup.find_all('a')

# 打印标题
print("标题:", title)

# 打印所有链接
print("链接:")
for link in links:
    print(link.get('href'))
