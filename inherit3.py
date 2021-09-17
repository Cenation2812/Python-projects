class A:
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def fun1(name):
        print(name)
    def fun2(self):
        print("Hello")

# @classmethod
# def fun3(name):
#     print(name)

obj = A("Dodo")
obj.fun1("KLKL")

obj.fun2()

#A.fun3("Dodo")
