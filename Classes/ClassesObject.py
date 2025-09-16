# OOP means object oriented programming
# classes and objects are the two main aspects of OOP
# a class is a blueprint for creating objects
# an object is an instance of a class
# a class can have attributes (variables) and methods (functions)

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    
    def __str__(self):
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, and {self.storage} storage"
    
    
