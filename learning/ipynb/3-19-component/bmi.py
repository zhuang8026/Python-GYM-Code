max = 24
min = 18.5
def bmi(w, h):
    return w/h**2
class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showProfile(self):
        print('My name is %s, I am %s years old.' % (self.name, self.age))