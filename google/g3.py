import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_yahoo_search(keyword, num_pages, num_results_per_page):
    base_url = "https://search.yahoo.com/search?p="
    search_url = base_url + keyword

    # 创建CSV文件
    with open(f'{keyword}_search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'URL', 'Content', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 循环遍历每一页搜索结果
        for page in range(1, num_pages + 1):
            # 发送HTTP请求
            response = requests.get(search_url + f"&b={(page - 1) * num_results_per_page}")

            if response.status_code == 200:
                # 使用Beautiful Soup解析网页内容
                soup = BeautifulSoup(response.text, 'html.parser')

                # 找到所有搜索结果项
                search_results = soup.find_all('div', class_='algo-sr')

                # 遍历搜索结果并提取信息
                for result in search_results[:num_results_per_page]:
                    try:
                        # 提取标题
                        title_element = result.find('h3', class_='title')
                        title = title_element.text.strip() if title_element else ""

                        # 提取URL
                        url_element = result.find('a')
                        url = url_element['href'] if url_element else ""

                        # 提取内容
                        content_element = result.find('span', class_='fc-falcon')
                        content = content_element.text.strip() if content_element else ""

                        # 提取日期
                        date_element = result.find('span', class_='fc-smoke')
                        date = date_element.text.strip() if date_element else ""

                        # 解析原始日期字符串并将其格式化为"年月日"的格式
                        # date_object = datetime.strptime(date, '%b %d, %Y')
                        # formatted_date = date_object.strftime('%Y年%m月%d日')

                        # 写入CSV文件
                        writer.writerow({'Title': title, 'URL': url, 'Content': content, 'Date': date})
                    except Exception as e:
                        print(f"An error occurred: {e}")
            else:
                print(f"Failed to fetch search results for page {page}")

    print(f"Search results for '{keyword}' saved to {keyword}_search_results.csv")

# 指定关键字、搜索页数和每页结果数量
keywords = ["近零建築示範應用"]  # "數據治理", "建築淨零", "近零建築示範應用", "Smart city", "Eco-city"
num_pages = 10
num_results_per_page = 10

# 执行搜索并保存结果到CSV文件
for keyword in keywords:
    scrape_yahoo_search(keyword, num_pages, num_results_per_page)
