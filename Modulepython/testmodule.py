# import mymodule as mmdl
from mymodule import person1

# mymodule.greeting("Alice")
# a = mymodule.person1['first_name']
# print(a)

print(person1['first_name'])
print(person1.items())


# use indent() to format the output
# json.dumps(x, indent=4)

# use separators to change the default separators
# json.dumps(x, indent=4, separators=(". ", " = "))

# use sort_keys to sort the result alphabetically by key
# json.dumps(x, indent=4, sort_keys=True)