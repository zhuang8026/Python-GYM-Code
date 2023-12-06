from abc import ABCMeta, abstractmethod

user = 'William test 001'
num = 33
timeout = '2021-05-01 12:00:00'

def getAPI(paload):
    print('Get API %s' % paload)

class Profile02(metaclass = ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def showProfile(self):
        pass


class GetUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showUser(self):
        print('My name is %s, I am %s years old.' % (self.name, self.age))


