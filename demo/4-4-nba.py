# PPT NBA

import requests;
from bs4 import BeautifulSoup;
import time;
import re;

# today = time.strftime("%Y-%m-%d", time.localtime());
today = time.strftime('%m/%d').lstrip('0'); # 去除字符串左邊的字符
                                            # 03/05 -> 3/05
# print(today)

def pttNBA(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤:' + url)
        return

    soup = BeautifulSoup(resp.text, 'html5lib')
    page_url = soup.find_all('div', {'class':'btn-group', 'class':'btn-group-paging'})[0].find_all('a')[1]['href']
    # print(page_url) # result: '/bbs/NBA/index1.html'

    items = []; 
    rent = soup.find_all('div', 'r-ent');
    for r in rent:
        title = r.find('div', {'class': 'title'}).text.strip(); # strip: 去除字符串兩側指定字符（預設是空白字符）
        count = r.find('div', 'nrec').text.strip();
        date = r.find('div', 'meta').find('div', 'date').text.strip();
        result = 'TIME: %s COUNT:%s TITLE: %s' % (date, count, title)

        try:
            if today == date and int(count) > 10:
                    items.append(result)
        except:
            if today == date and count == '爆':
                items.append(result)
    print(len(items))
    if len(items) != 0:
        for i in items:
            print(i);
        pttNBA('https://www.ptt.cc' + page_url)
    else:
        return;

# 執行
pttNBA('https://www.ptt.cc/bbs/NBA/index.html')