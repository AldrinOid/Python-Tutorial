# class and instance of a recipe

class Recipe:
    def __init__(self, name, items, time):
        self.name = name
        self.items = items
        self.time = time
    
    def Food(self):
        return f"The recipe for {self.name} requires {self.items} and takes {self.time} minutes to prepare."

pizza = Recipe("Pizza", ["dough", "sauce", "cheese"], 30) 
burger = Recipe("Burger", ["bun", "patty", "lettuce"], 15)
spaghetti = Recipe("Spaghetti", ["pasta", "sauce", "meatballs"], 20)

def main():
    print(pizza.Food())
    print("\n")
    print(burger.Food())
    print("\n")
    print(spaghetti.Food())

main()