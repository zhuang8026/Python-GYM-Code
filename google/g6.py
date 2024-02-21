from googlesearch import search
from bs4 import BeautifulSoup
import csv
import requests
import datetime

# 定义函数用于爬取并保存数据
def scrape_and_save(keyword, num_results):
    # 定义空列表用于存储结果
    data = []
    
    # 执行搜索并遍历搜索结果
    for url in search(keyword, stop=10, pause=2.0):
        # 发送HTTP请求获取页面内容
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取标题
        title = soup.title.string if soup.title else ""
        # title_element = soup.find('h3', class_='title')
        # title = title_element.text.strip() if title_element else ""
        print(title)
        # 提取内容
        # content = ""
        # for paragraph in soup.find_all('p'):
        #     content += paragraph.get_text()
        
        # 提取日期
        # date = datetime.datetime.now().strftime('%Y-%m-%d')
        
        # 将结果添加到列表中
        # data.append({'Title': title, 'URL': url, 'Content': content, 'Date': date})
    
    # 将结果列表转换为DataFrame
    with open(f'{keyword}_search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'URL', 'Content', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# 指定关键字列表和每个关键字搜索结果数量
keywords = ["近零建筑示范应用"] # "數據治理", "建築淨零", "近零建筑示范应用", "Smart city", "Eco-city"
num_results_per_keyword = 40

# 循环遍历关键字列表并执行爬取和保存数据的操作
for keyword in keywords:
    scrape_and_save(keyword, num_results_per_keyword)
