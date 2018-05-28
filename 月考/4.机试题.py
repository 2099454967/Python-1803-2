from random import randint
class tool(object):
    def __init__(self):
        self.list = []
    def add(self):
        for i in range(10):
            while True:
                i = randint(1,100)
                if i not in self.list:
                    self.list.append(i)
                    break
        print(self.list)
    def function1(self):
        self.list.sort()
        print(self.list)
    def function2(self):
        pass
num = tool()
num.add()
num.function1()
num.function2()

