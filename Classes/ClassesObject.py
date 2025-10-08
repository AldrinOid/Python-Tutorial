# OOP means object oriented programming
# classes and objects are the two main aspects of OOP
# a class is a blueprint for creating objects
# an object is an instance of a class
# a class can have attributes (variables) and methods (functions)

# class Computer:
#     def __init__(self, cpu, ram, storage):
#         self.cpu = cpu
#         self.ram = ram
#         self.storage = storage
    
#     def __str__(self): # default message
#         return f"Computer with {self.cpu} CPU, {self.ram} RAM, and {self.storage} storage"
    
#     def add_number(self, a, b):
#         return a + b

# p1 = Computer("Intel i7", "16GB", "512GB SSD")
# print (p1) # printing the default message
# print(p1.add_number(5, 10))



# class Student: # create class
#     def __init__(self, name = "Unknown", year = "Not Assigned", course = "Not Assigned", section = "Not Assigned"): # initialize the mainly use parameters 
#         # you can add default values in these parameters to make your code readable and understandable 
#         self.name = name # this is attributes
#         self.year = year # this is attributes
#         self.course = course # this is attributes
#         self.section = section # this is attributes
    
#     def nameYear(self, name, year): # this is method and in every method ther should be self as a current object. you can access the attributes you initialize in the first method. self is the only parameter if you want your attributes stay at it's default value
#         print(f"My name is: {name} and I'm {year} college")
    
#     def courseSection(self, course, section, happy, name): # this is method and in every method ther should be self as a current object. you can access the attributes you initialize in the first method. you can add here another parameter if you want
#         print(f"I'm taking {course} from {section} and I'm {happy} and My name is {name}")
    
# student1 = Student() # create object and you can now access the methods inside this class

# student1.nameYear("Michael", "4th Year") # your created object are now accessing the methods inside the class

# student1.courseSection("Computer Science", "4-Y1-1", "yes", "luke")


# class Car:
#     def __init__ (self, brand, model, year, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
    
#     def carInfo(self):
#         print(f"This car is a {self.color} {self.year} {self.brand} {self.model}")
    
#     def isVintage(self):
#         if int(self.year) < 2000:
#             print("This is a vintage car.")
#         else:
#             print("This is modern car.")
    
#     def updateColor(self, color):
#         self.color = color
#         print(f"Car color has been updated to {self.color}")

# car1 = Car("Innova", "Toyota", "2020", "Red")

# car1.carInfo()
# car1.isVintage()
# car1.updateColor("Black")
# car1.carInfo()


class BankAccount:
    def __init__(self, account_name, balance = 0):
        self.account_name = account_name
        self.balance = balance
        self.transaction = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(f"Deposited: {amount}. New Balance: {self.balance}")
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.transaction.append(f"Withdraw: {amount}. New Balance: {self.balance}")
            print(f"Withdraw: {amount}. New Balance: {self.balance}")
        else:
            self.transaction.append(f"Insufficient funds. Current Balance: {self.balance}")
            print(f"Insufficient funds. Current Balance: {self.balance}")
    
    def displayBalance(self):
        print(f"Account: {self.account_name}. Balance: {self.balance}")
    
    def transfer(self, other_account, amount):
        if self.balance > amount:
            self.balance -= amount
            other_account.balance += amount
            self.transaction.append(f"Transfer {amount} from {self.account_name} to {other_account.account_name}. New Balance: {self.balance}")
            other_account.transaction.append(f"Received {amount} from {self.account_name} New Balance: {other_account.balance}")
            print(f"Transfer {amount} from {self.account_name} to {other_account.account_name}")
        else:
            self.transaction.append(f"Insufficient funds. Current Balance: {self.balance}")
            print(f"Insufficient funds. Current Balance: {self.balance}")
        
    def showTransactionHistory(self):
        print(f"Transaction History for {self.account_name}:")
        if not self.account_name:
            print("No Transaction Yet")
        else:
            for transaction in self.transaction:
                print("-", transaction)



acc1 = BankAccount("Aldrin", "1000")
acc2 = BankAccount("Jesserie", 500)
print()
acc1.displayBalance()
acc2.displayBalance()
print()
acc1.deposit(300)
acc2.deposit(200)
print()
acc1.displayBalance()
acc2.displayBalance()
print()
acc1.transfer(acc2,300)
print()
acc1.displayBalance()
acc2.displayBalance()
print()
acc1.withdraw(1200)
acc2.withdraw(800)
print()
acc1.displayBalance()
acc2.displayBalance()
print()
acc1.showTransactionHistory()
acc2.showTransactionHistory()


    
    
