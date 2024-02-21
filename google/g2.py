import os
import sys
import requests
from bs4 import BeautifulSoup
import re

# 安装 googlesearch-python 模块
try:
    import googlesearch
except ImportError:
    print("正在安装 googlesearch-python 模块...")
    os.system('pip install googlesearch-python')

from googlesearch import search

def get_google_results(query):
    try:
        results = search(query, num_results=10, lang='zh-tw')
        
        with open("google_search_results.txt", "w", encoding="utf-8") as f:
            for i, result in enumerate(results, 1):
                title, timestamp = get_title_and_timestamp(result)
                f.write(f"Result {i}:\nTitle: {title}\nTime: {timestamp}\nLink: {result}\n\n")
        
        print("搜尋結果已保存到 google_search_results.txt 中。")
    except Exception as e:
        print("抓取搜尋結果时发生错误:", e)

def get_title_and_timestamp(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        # 获取每个搜索结果中显示的时间，假设在标题元素的下一个兄弟元素中
        timestamp = extract_timestamp(soup.title.find_next_sibling().text)
        return title, timestamp
    except Exception as e:
        print("提取标题和时间时发生错误:", e)
        return "无法获取标题", "无法获取时间"

def extract_timestamp(text):
    # 在文本中使用正则表达式匹配时间格式，这里以简单示例为例
    match = re.search(r'\d{4}年\d{1,2}月\d{1,2}日', text)
    return match.group(0) if match else "No timestamp found"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供要搜索的词语作为参数。")
    else:
        query = " ".join(sys.argv[1:])
        get_google_results(query)
