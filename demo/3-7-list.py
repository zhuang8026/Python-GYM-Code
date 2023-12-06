# * 用中括弧將資料包起來，並且用逗號分隔
    # -> [9,99,9]
# * 在中括弧裡面輸入索引值，取出數值
    # -> array[1] 
# * 使用冒號選取索引值的範圍
    # -> array[3:7] 包含3,不包含7

list1 = [3,1,5,4,2]
print(list1[2]) # result: 2
print(list1[:3]) # result: [3,1,5], 不包含結束位置的資料（key: 3）
print(list1[1:3]) # result: [1,5], 包含起始位置的資料（key: 1）不包含結束位置的資料（key: 3）
print(list1[2:]) # result: [5, 4, 2], 包含起始位置的資料（key: 2）

# ---------------- 
list2 = [6,7]
list1.append(999999) # result: [3, 1, 5, 4, 2, 999999]
list1.append(list2) # append 附加的意思
print(list1) # result: [3, 1, 5, 4, 2, [6, 7]]

list3 = [33,44]
list1.extend(list3) # result: [3, 1, 5, 4, 2, [6, 7], 33, 44]
                    # extend 延伸的意思
print(list1) # result: [3, 1, 5, 4, 2, 999999, [6, 7], 33, 44]

# ---------------- 
list1.pop(5) # pop 是移除索引值的意思
print(list1) # result: [3, 1, 5, 4, 2, [6, 7], 33, 44]

list1.remove(5) # remove 是移除指定值的意思
print(list1) # result: [3, 1, 4, 2, [6, 7], 33, 44]

# ---------------- 

list4 = [1,2,3,4,5,6,7,8,9]
list4.reverse(); # reverse 是反轉的意思
print(list4)

list5 = [6,3,1,9,6,4,3,2,7,8]
list5.sort(reverse=True) # sort 是排序的意思
                         # everse=True 是降冪, 反之為升冪
print(list5) # result: [1, 2, 3, 3, 4, 6, 6, 7, 8, 9]