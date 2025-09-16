class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    
    def check_specs(self):
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, and {self.storage} storage"
    
    def check_performance(self):
        return "Performance is good"
    
    def check_storage(self):
        return "Storage is sufficient"

class Laptop(Computer):
    def __init__(self, cpu, ram, storage, weight):
        super().__init__(cpu, ram, storage)
        self.weight = weight
    
    def check_weight(self):
        return f"Laptop weight is {self.weight} kg"

l1 = Laptop("Intel i7", "16GB", "512GB SSD", 1.5)
print(l1.check_specs())
print(l1.check_weight())
print(p1.check_specs())
print(p1.check_performance())

p1 = Computer("Intel i7", "16GB", "512GB SSD")
print(p1.check_specs())
print(p1.check_performance())
print(p1.check_storage())
