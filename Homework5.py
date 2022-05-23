class car:
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.brand = "Ford Mustang"
        self.price = "10000000$"
class avto:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.engine = "Electric"
class vehicle:
    pass
class Mustang_car(car, avto, vehicle):
    def car_info(self):
        print("Car info(BMW X10):")
        print("Бренд авто:",self.brand)
        print("Ціна авто:",self.price)
        print("Тип авто:",self.engine)

Mustang = Mustang_car()
Mustang.car_info()