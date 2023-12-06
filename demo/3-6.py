def sayHello(name = 'Allen', age = '99'):
    print("Hello " + name + "!" + " " + "I'm " + str(age) + " years old.");

sayHello('william', 18);
sayHello(age='11', name='Billiam');

# 傳入多個參數
def foo(*payload): # * 代表傳入多個參數
    print(payload);

foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
