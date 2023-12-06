## 集合(Set)
# * 集合內的元素不能重複，也沒有順序性，無法使用索引值取值
# * 用大括弧包起來，並且用逗號分隔
# * 聯集( | )
# * 交集( & )
# * 差集( - )
# * 排除相同元素( ^ )

V = {'a', 'e', 'u', 'i', 'o'}
F = {'d', 'n', 'g', 'i', 'o'}

print(V | F) # 聯集 result: {'a', 'i', 'e', 'g', 'o', 'u', 'd', 'n'}, 
print(V & F) # 交集 result: {'o', 'i'}, 
print(V - F) # 差集 result: {'u', 'e', 'a'}, 
print(V ^ F) # 排除相同元素 result: {'g', 'e', 'a', 'u', 'd', 'n'}

a = {1, 2, 3, 4}
# 新增單一
a.add(5)
print(a) # result: {1, 2, 3, 4, 5}
# 新增多個
a.update({ 6,7,8,9,10,11,23,4,56,7 })
print(a) # result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 56}
# 刪除
a.remove(3)
print(3 in a) # result: False
print(a) # result: {1, 2, 4, 5}
a.discard(5)
print(a) # result: {1, 2, 4}
print(5 in a) # result: False
#刪除多個
a.difference_update({1, 2, 4, 6, 8, 9, 10, 11, 23, 56})
print(a) # result: {7}

# remove & discard差異
# 當 刪除沒有的值時（ex: 999）
a.remove(999) #  “remove” 會拋出 KeyError
a.discard(999) # “discard” 不會拋出 KeyError