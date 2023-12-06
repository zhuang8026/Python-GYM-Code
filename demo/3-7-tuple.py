# * 使用小括弧將資料包起來
# * Tuple 中的內容不可變動
# * Tuple 元組，以確保這些數據不會被修改

t = (3,1,5,2,4)
print(t) # result: (3, 1, 5, 2, 4)
list4 = list(t) # 用list函式, 將 tuple 轉成 list 物件
print(list4) # result: [3, 1, 5, 2, 4]
print(type(list4)) # result: <class 'list'>


### List和Tuple 共用 的函式 與 關鍵字
arr = (3,1,5,2,4,2)
# in 函式: 檢查元素是否在tuple中
print(5 in arr) # result: True  
print(6 in arr) # result: False

# len() 函式: 取得tuple的長度
print(len(arr)) # result: 5

#count() 函式: 取得元素出現的次數
print(arr.count(2)) # result: 2