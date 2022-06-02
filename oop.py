# cust id
# name
# balance

# desposite
# withdraw

#1 how to create class, object
#2 how to define instance variable
#3 how to apply instance variable as private

#static method

#inheritance
from itertools import count


class Account:
    #default arg must be self
    #self.__id (private)

    count = 0   #for count

    #decorator
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    #static method
    @staticmethod
    def print_Val():
        print("Static method is account class")

    def __init__(self,cust_id,name,initial_bal=0) -> None:
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_bal
        Account.increment_count()
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def deposite(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
        return self.__balance
customer1 = Account("101","ABC")
# Account(customer1,"101","ABC")
# print(customer1)

customer2 = Account("102","DEF")
# print(customer1)

customer3 = Account("103","XYZ")
# print(customer1)

#for private , _Account__id
print(customer1._Account__id,customer1._Account__name,customer1._Account__balance)

#__dict__
print(customer1.__dict__)
print(customer1.get_balance())
print(customer1.deposite(50000))
print(customer1.withdraw(10000))
customer4 = Account("104","RST")
customer2.deposite(8000)
customer3.deposite(10000)
customer4.deposite(70000)

l = [customer1,customer2,customer3,customer4]

for obj in l:
    if obj.get_balance() < 10000:
        print(obj.get_id(),obj.get_name())

# print(Account.count)
# print(customer1.count)
# print(customer2.count)

# Account.count +=5
# print(Account.count)
# print(customer1.count)
# print(customer2.count)

# customer1.count = 100
# print(Account.count)
# print(customer1.count)
# print(customer2.count)
# #only cust2 count change

# print(Account.__dict__)
# print(customer2.__dict__)

print(Account.get_count())

#static method can call directly.
Account.print_Val()

#Inheritance

class Saving_Account(Account):
    def __int__(self,id,name,initial_bal=0):
        #super 
        super().__init__(id,name,initial_bal)
        self.limit = 50000
    
    def withdraw(self, amount):
        if amount < self.limit:
            new_bal = super().withdraw(amount)
            self.limit -=amount
            return new_bal
        else:
            print("Daily limit reached")
 
cust1 = Saving_Account(105,"ARG")
print(cust1.__dict__)
# help(customer1)
print(cust1.deposite(80000))
print(cust1.withdraw(40000))
