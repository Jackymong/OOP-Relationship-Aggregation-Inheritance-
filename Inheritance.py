#Single inheritance
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(12000,"Apple",13)
s.buy()


#Multi level inheritance
class Product:
    def review(self):
        print("Customer Review for Product")
        
class Phone(Product):
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = cemera

    def buy(self):
        print("Buying phone")


class SmartPhone(Phone):
    pass

s = SmartPhone(12000,"Apple",13)
p = Phone(1000,"Samsung", 12)
s.buy()
s.review()
p.review()


#Hierarchical inheritance
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

s = SmartPhone(12000,"Apple",13).buy()


#Multiple inheritance and MRO(Method resulation order)
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class Product:
    def review(self):
        print("Customer Review")

    def buy(self):
        print("Buying phone from product")

class SmartPhone(Product,Phone):
    pass

s = SmartPhone(12000,"Apple",13)
s.buy()
s.review()




#inheriting constructor
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

s = SmartPhone(12000,"Apple",13)
print(s.brand)




#Inheriting Private Members
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s = SmartPhone(12000,"Apple",13)
s.check()



#Practice
class A:
    def __init__(self):
        self.var1 = 100

    def display1(self,var1):
        print("Class A",var1)

class B(A):

    def display2(self,var1):
        print("Class B",self.var1)

obj = B()
obj.display1(200) 



#Use supper keyward
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = cemera

    def buy(self):
        print("Buying phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
        super().buy()

s = SmartPhone(12000,"Apple",13)
s.buy()
