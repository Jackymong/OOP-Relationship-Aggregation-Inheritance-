class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_pro(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_add(new_city,new_pin,new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_add(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

add = Address("Dhaka",1234,"DHA")
cus = Customer("Jacky","Male",add)

cus.edit_pro("Jami","Chittagong",2345,"CTG")

print(cus.address.pincode)
