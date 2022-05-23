class Computer:
    modeldef __init__(self,model,*args,**kwargs):
    def calculate(*args,**kwargs):
        print("Calculating...")
class Display:
    def display(self):
        print("I display the image on the screen...")
class Phone:
        def call(self):
            print("caling...")
class SmartPhone(Display,Computer,Phone):
    pass
iphone = SmartPhone()
iphone.calculate()
iphone.display()
iphone.call()








#class Class1:
#    var = 20
#    def __init__(self):
#        self.var=10
#class Class2(Class1):
#    def __init__(self):
#        print(self.var)
#        super().__init__()
#        print(self.var)
#        print(super().var)
#obj = Class2()







#class Hello:
#    def __init__(self):
#        print("Hello")
#class HelooWorld(Hello):
#    def __init__(self):
#        super().__init__()
#        print("World")
#helW = HelloWorld()