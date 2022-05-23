class Student:
    a = 0
    def __init__(self):
        self.hp = 100
        self.speed = 25
        self.money = 100000
        self.reyting = 3
        self.mark = 12
    def p(a):
        print("Best student:")
Vasia = Student()
Vasia.p()
Vasia.reyting = 2
Vasia.mark = 11

Ksusha = Student()
Ksusha.hp = 50
Ksusha.money = 900000
Ksusha.reyting = 1
Ksusha.mark = 12

Max = Student()
Max.speed = 200
Max.money = 900000
Max.mark = 10

print("Vasia hp:", Vasia.hp, "Vasia speed:",Vasia.speed, "Vasia money:", Vasia.money, "Vasia reyting:", Vasia.reyting, "Vasia mark",Vasia.mark)
print("Ksusha hp:",Ksusha.hp, "Ksusha speed:",Ksusha.speed,"Ksusha money:", Ksusha.money, "Ksusha reyting:", Ksusha.reyting, "Ksusha mark",Ksusha.mark)
print("Max hp:",Max.hp, "Max speed:",Max.speed,"Max money:", Max.money, "Max reyting:", Max.reyting, "Max mark",Max.mark)
