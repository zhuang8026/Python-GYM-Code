import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义函数用于爬取并保存数据
def scrape_and_save(keyword, num_pages):
    # 定义空列表用于存储结果
    data = []
    
    # 循环遍历每一页搜索结果
    for page in range(1, num_pages + 1):
        # 构造Google搜索的URL
        url = f"https://www.google.com/search?q={keyword}" # &start={(page-1)*10}

        # 发送HTTP请求
        response = requests.get(url)
        # print(response)
        # 使用Beautiful Soup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有搜索结果
        search_results = soup.find(id="center_col")
        print(search_results)
        # 遍历搜索结果并提取信息
        for result in search_results:
            # print(result)
            try:
                title = result.find('h3').text
                url = result.find('a')['href']
                content = result.find('span').text
                date = result.find('span').text.split(' · ')[0]

                # print(date)
                # print(title)
                # print(url)
                # print(content)
                

                # 将结果添加到列表中
                data.append({'Title': title, 'URL': url, 'Content': content, 'Date': date})
            except:
                pass
    
    # 将结果列表转换为DataFrame
    df = pd.DataFrame(data)
    
    # 将DataFrame保存为UTF-8编码的CSV文件
    df.to_csv(f'{keyword}_search_results.csv', index=False, encoding='utf-8-sig') 

# 指定关键字和搜索页数
keyword_list = ["數據治理"] # "建築淨零", "示範應用", "Smart city", "Eco-city"
num_pages = 10

# 循环遍历关键字列表并执行爬取和保存数据的操作
for keyword in keyword_list:
    scrape_and_save(keyword, num_pages)
