"""                 intro about class

class Item:
    def calculate_total_price (self, x, y):  #function inside the class is "Method"   #! And we can't create method with null parameters
        return x * y


item1 = Item()
# Assign attribute to instances
item1.name = 'Phone'    #Create class attribute "name" and give value "Phone" to it
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))   #! When call method from an instance, Python will pass the object itself as the first argument "Every Time"

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

"""









"""                 How to use __init__
# the original method the start and end with "__" will call "magic method"

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self,name: str, price, quantity=0):    #! you can set default value or expected data type to the parameters
        #! Run validations to the received arguments and set the error message when the validations is false
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)   #! add "self" to "all" list

    def calculate_total_price (self, x, y): 
        return x * y
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate     #! instance level (self) and class level (Item)
        self.price = self.price * self.pay_rate

    def __repr__(self):      #! Representing your object เพื่อแก้ปัญหา Print ออกมาแล้วเจอหน้าตาประมาณนี้ [<__main__.Item object at 0x000001A68EFDBFD0>]
        return f"Item ('{self.name}', {self.price}, {self.quantity})\n"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)



'''     printing the object in "all" list
for instance in Item.all: 
    print(instance.name)
'''
print(Item.all)

# print(Item.__dict__)    #! Print all the attributes for class level
# print(item2.__dict__)    #! Print all the attributes for instance level  (not include "pay_rate")
"""








"""                 Class vs Static Methods

import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self,name: str, price, quantity=0):
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price (self, x, y): 
        return x * y
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate   
        self.price = self.price * self.pay_rate

    @classmethod    #! send the object at the first argument
    def instantiate_from_csv(cls):      #! cls is the class reference must be passed as a first argument (reference to the class itself)
        path = 'E:\Work\Coding\Python\Learn\OOP\\freecodecamp\\item.csv'
        with open(path, 'r') as f:    #! 'with' is used to create a context in which a file is opened and managed properly and open(filename, permission,) as variable
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod   #! not send the object at the first argument
    def is_integer(num):
        # We will count out the floats that are point zero]
        # For i.e : 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})\n"
    
Item.instantiate_from_csv()
print(14,Item.is_integer(14.0))

"""


















"""                 Inheritance
"""

import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self,name: str, price, quantity=0):
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price (self, x, y): 
        return x * y
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate   
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls): 
        path = 'E:\Work\Coding\Python\Learn\OOP\\freecodecamp\\item.csv'
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero]
        # For i.e : 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity})\n"

class Phone(Item):      #! Inheit from Item (This is a child class)

    def __init__(self,name: str, price, quantity=0, broken_phone=0):

        #! Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        
        assert broken_phone >= 0, f'Broken Phones {broken_phone} is not greater or equal to zero!'

        self.broken_phone = broken_phone


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())       #! Use the method from the parent class
phone2 = Phone("jscPhone20", 700, 5, 1)