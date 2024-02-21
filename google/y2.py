import requests
from bs4 import BeautifulSoup
import csv

def scrape_yahoo_search(keyword, num_results):
    base_url = "https://search.yahoo.com/search?p="
    search_url = base_url + keyword

    # 发送HTTP请求
    response = requests.get(search_url)

    if response.status_code == 200:
        # 使用Beautiful Soup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有搜索结果项的标题
        titles = soup.find_all('h3', class_='title') 

        # 创建CSV文件
        # with open(f'{keyword}_search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        #     fieldnames = ['Title']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()

        # 遍历标题并写入CSV文件
        for title in titles[:num_results]:
            try:
                # 提取标题文本
                title_text = title.text.strip()
                print(title_text)
                # 写入CSV文件
                # writer.writerow({'Title': title_text})
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # 如果发生异常，继续执行下一次循环

        # print(f"Search results titles for '{keyword}' saved to {keyword}_search_results.csv")
    else:
        print("Failed to fetch search results")

# 指定关键字和搜索结果数量
keywords = ["數據治理"] # "建築淨零", "示範應用", "Smart city", "Eco-city"
num_results = 100

# 执行搜索并保存标题到CSV文件
for keyword in keywords:
    scrape_yahoo_search(keyword, num_results)
