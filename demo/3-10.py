# for迴圈和while迴圈

# for迴圈取得容器型態元素的用法
# for 變數 in 容器型態 ：
    # 容器內元素依序放入變數中取出
names = ['Mary', 'Sam', 'David']
for s in names:
    print(s) # result: Mary, Sam, David

dict = { 'a':1, 'b':2, 'c':3 }

# --------- for in ---------
for key in dict.keys():
    print(key) # result: a, b, c

for val in dict.values():
    print(val) # result: 1, 2, 3

for key in dict.keys():
    print(dict[key]) # result: 1, 2, 3

for obj in dict.items():
    arr = list(obj) # 轉可編輯物件
    arr[1] = arr[1] + 4
    print(obj) # result: ('a', 1), ('b', 2), ('c', 3)
    print(arr) # result: ['a', 5], ['b', 6], ['c', 7]


# --------- range ---------
for i in range(1, 10, 2): # rang(起始值, 結束值, 累加值)
                          # 累加值: 起始值 + 累加值 = 下一步迴圈參數
    if i == 3: # 因為 1+ 2 = 3, 所以條件達成, 跳出迴圈
        break;
    print(i) 

for i in range(1, 10, 2): # rang(起始值, 結束值, 累加值)
                          # 累加值: 起始值 + 累加值 = 下一步迴圈參數
    if i == 3: # 因為 1+ 2 = 3, 所以條件達成, 跳出迴圈
        continue;
    print(i) 

# --------- while ---------

import random # PY 匯入隨機

n = random.randint(1,5) # 隨機 整數
num = int(input('請輸入整數(1~10):')) # 輸入 整數

while n != num: # 條件
    if num<n:
        print('你猜的數字比較小')
        num = int(input('請輸入1到10之間的一個數字:'))
    elif num>n:
        print('你猜的數字比較大')
        num = int(input('請輸入1到10之間的一個數字:'))
    else:
        break;
print('你猜對了！')