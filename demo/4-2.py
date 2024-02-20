import requests; # python 3716 framework
from bs4 import BeautifulSoup;  # python 3716 framework

resp = requests.get('https://code-gym.github.io/spider_demo/');
soup = BeautifulSoup(resp.text, 'html5lib'); # python 3716 framework: "html5lib"

# print(soup.find('h1'));
# print(soup.find('h1').text);
# print(soup.h1.text);

res = soup.find_all('h3', 'post-title'); # 找到所有h3標籤，並且class-name為 "post-title"
for h3 in res:
    print(h3.a)


for cat in soup.find_all('a',{'class':'post-category', 'class':'cat-1'}):
    print(cat)

for post in soup.find_all('div'):
    print(post);

for post in soup.find_all('footer'):
    print(post);

for post in soup.find_all('div', 'post-body'):
    for str in post.stripped_strings: # 'stripped_strings' 只取得字串，標籤全部去除
        print(str)

print('-----')
for post in soup.select('#footer'):
    print(post)
print('-----')

# 選擇所有具有 id 屬性的元素
all_elem = soup.select('[id]')
# 遍歷所有符合選擇器的元素
for element in all_elem:
    print(element)
    print(element.get('id'))

nav = soup.find(id = 'nav')
print(nav)