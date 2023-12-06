from bmi import *
from will import *

import math
# 第二種用法：from math import gcd, fsum

# print(dir(math)) # list all methods in math
print(math.gcd(6, 3))

print(max)

print(bmi(65, 1.75))
pro = Profile('Ryan', '18')
pro.showProfile()

print(user, num, timeout);

getAPI('3.1415926Q')

# 建立物件
getUser = GetUser("BILLIAM", 18);
getUser.showUser();

# #繼承 抽象類別
class GetUser02(Profile02):
    def __init__(self, name, age, ID):
        self.name = name;
        self.age = age;
        self.ID = ID;
    def showProfile(self):
        print('My name is %s, I am %s years old. My ID is %d' % (self.name, self.age, self.ID))

gUser = GetUser02("Billiam", 18, 2099999);
gUser.showProfile();
