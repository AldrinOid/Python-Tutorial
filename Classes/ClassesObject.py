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



class Student: # create class
    def __init__(self, name = "Unknown", year = "Not Assigned", course = "Not Assigned", section = "Not Assigned"): # initialize the mainly use parameters 
        # you can add default values in these parameters to make your code readable and understandable 
        self.name = name # this is attributes
        self.year = year # this is attributes
        self.course = course # this is attributes
        self.section = section # this is attributes
    
    def nameYear(self, name, year): # this is method and in every method ther should be self as a current object. you can access the attributes you initialize in the first method. self is the only parameter if you want your attributes stay at it's default value
        print(f"My name is: {name} and I'm {year} college")
    
    def courseSection(self, course, section, happy): # this is method and in every method ther should be self as a current object. you can access the attributes you initialize in the first method. you can add here another parameter if you want
        print(f"I'm taking {course} from {section} and I'm {happy} and My name is {self.name}")
    
student1 = Student() # create object and you can now access the methods inside this class

student1.nameYear("Michael", "4th Year") # your created object are now accessing the methods inside the class

student1.courseSection("Computer Science", "4-Y1-1", "yes")



    
    
