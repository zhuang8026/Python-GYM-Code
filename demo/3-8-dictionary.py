# dictionary 是字典的意思，顧名思義就是 key: value 的結構，因為像字典一樣，找開頭的 key 會比較快
# key 不能重複
# 用法： {key: value}
dict = {
    'name': 'Allen',
    'age': 99, 
    # 'age': 100 # 這行會報錯 
}
print(dict) # result: {'name': 'Allen', 'age': 99}  
print(dict['name']) # result: Allen

test = dict.get('banana', 'NO DATA') # 如果沒有這個 key，就會回傳 NO DATA 
print(test) # result: NO DATA


dict2 = { (2,3):'A', (5,-3):'B', (-1,-5):'C' }
test1 = dict2[(5,-3)] # 指定Key值，取得Value    
print(test1) # result: B

print(dict2.keys()) # 取得所有的 key, dict_keys([(2, 3), (5, -3), (-1, -5)])
print(dict2.values()) # 取得所有的 value, dict_values(['A', 'B', 'C'])
print(dict2.items()) # 取得所有的 key-value, dict_items([((2, 3), 'A'), ((5, -3), 'B'), ((-1, -5), 'C')])

# 修改字典
# 新增
dict2['bbbb'] = 9999999999
print(dict2) # result: {(2, 3): 'A', (5, -3): 'B', (-1, -5): 'C', 'bbbb': 9999999999}
# 修改
dict2[(5, -3)] = 'BB FFFFFF'
print(dict2) # result: {(2, 3): 'A', (5, -3): 'BB FFFFFF', (-1, -5): 'C', 'bbbb': 9999999999}
# 單獨清空
del dict2[(5, -3)]
print(dict2) # result: {(2, 3): 'A', (-1, -5): 'C', 'bbbb': 9999999999}
# 全部清空
dict2.clear() # 清空
print(dict2) # result: {}

