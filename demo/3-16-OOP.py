# 物件導向 之 類別

# 類別
class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print('Hello, my name is', self.name)
        print('I am', self.age, 'years old')

    @staticmethod
    def getUser(name): {
        print('Hello, my name is', name)
    }

# 物件
p1 = Persion('John', 36) # 創建 Person 類的實例
p1.say_hi() # 呼叫方法
p1.getUser('William') # 呼叫靜態方法

print('-------------------')
# -------- 繼承 --------
# 可建立物件之間彼此關係的專有名詞： 繼承
# 可重複選寫共同屬性

class Student(Persion):
    def __init__(self, name, age, sid):
        # super() 代表父類別, 繼承父類別的屬性
        # 將 name 和 age 放入 super() 中
        super().__init__(name, age)
        self.sid = sid
    def showStudentID(self):
        print('我的學號是:', self.sid)
    @staticmethod
    def staticTest(val):
        print('staticTest: %d' % val)

# 創建 Person 類的實例
sut = Student('John', 36, 22000400);
# 呼叫方法
sut.say_hi()
sut.showStudentID()
# 呼叫靜態方法
sut.getUser('William')
Student.getUser('William') # 呼叫 父類別 靜態方法
Student.staticTest(123) # 呼叫 子類別 靜態方法



