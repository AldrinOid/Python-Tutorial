# accessing items in dictionaries
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020
}

x = thisdict["model"]
y = thisdict.get("year")
print(x)
print(y)

# accessing keys
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020
}
x = thisdict.keys()
print(x)
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020,
    "color" : "red"
}
x = thisdict.keys()
print(x)

# accessing the values
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020
}
x = thisdict.values()
print(x)
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020,
    "color" : "red"
}
x = thisdict.values()
print(x)

# accesing the item
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020
}
x = thisdict.items()
print(x)
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020,
    "color" : "red"
}
x = thisdict.items()
print(x)

# check if the key is exists
thisdict = {
    "brand" : "Toyota",
    "model" : "innova",
    "year" : 2020
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")






