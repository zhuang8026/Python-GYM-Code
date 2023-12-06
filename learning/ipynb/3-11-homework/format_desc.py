name = 'Python'
age = 27

# 字符串格式化
# 打印 "我是Python,今年27岁了"

new_str = "1. 我是" + name + "," + "今年" + str(age) + "岁了"
# 字串 + 數字 = Error
# str() 將number 轉 字串

print(new_str)

# 計算 字符串 長度
print("字符串name長度:" + str(len(name)));

# 注意：
new_str_1 = "2. 我是%s,今年%d岁了" % (name, age)
# % => 必須是字串 or 整數

print(new_str_1)

new_str_2 = "3. 我是{name},今年{age}岁了".format(
    name='aaaa', age=1.111111111111111111111
)
#[推薦一] {xxx} format(xxx='xzcc' or xxx=1.0987654321) 此方法，通吃
print(new_str_2)

name1 = 'abc'
age1 = 30

new_str_3 = f"4. 我是{name1},今年{age1}岁了"
new_str_4 = f'''4. 我是'{name1}',今年"{age1}"岁'''
new_str_4_1 = f"4. 我是'{name1}',今年\"{age1}\"岁"
#[推薦二] f => 可直接引用外面的變量

print(new_str_3)
print(new_str_4)
print(new_str_4_1)

new_str_5 = f"abc\nefg";
print(new_str_5);
print(new_str_5[0]);
print(new_str_5[-1]);
print(len(new_str_5)); #len是計算長度

a1 = '1'
a2 = 'abc'
b = '2'
c = 3
# print(a * b); # Error 字串不能乘字串
print(a1 * c); # Success >> 111
print(a2 * c); # Success >> abcabcabc