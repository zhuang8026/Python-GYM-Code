# 物件導向 之 抽象類別
# 重點
    # -> 抽象類別 不能建立實例（不能建立物件）
    # -> 子類別 繼承 抽象類別 必須實作裡面所有的抽象函式
    # -> 抽象類別 中尚未實作的方法，稱為 抽象方法

from abc import ABCMeta, abstractmethod; # 抽象類別

# 抽象類別：父類別
class Employee (metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 一般方法
    def say_hi_1(self):
        print('Hello, my name is %s and %d years old' % (self.name, self.age) )

    # 抽象方法（子類別必須實作）
    @abstractmethod
    def say_hi(self):
        pass

    # 抽象函式： 抽象類別中的靜態方法
    # 注意：要有“@abstractmethod”才是 抽象方法
    @abstractmethod
    def showUserID(): 
        pass 

# 子類別
class Teacher(Employee):
    def __init__(self, name, age, tid):
        super().__init__(name, age)
        self.tid = tid
    
    # 注意：子類別一定要實作父類別的抽象函式
    def showUserID(self):
        print('我的工號是:', self.tid)

    def say_hi(self):
        print('我是抽象靜態類別的sayhi函式: %s' % self.name)

# 子類別
teacher = Teacher('Allen', 2000, '123456789')
teacher.showUserID(); #子類別繼承父類別的靜態方法
teacher.say_hi(); # 子類別繼承父類別的抽象方法
