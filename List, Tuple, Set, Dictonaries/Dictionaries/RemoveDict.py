# removing items from dictionary

thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
thisdict.pop("model")
print(thisdict)

# using popitem() method to remove last inserted item
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "color": "red"
    }
thisdict.popitem()
print(thisdict)

# using del keyword to remove item
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "color": "red"
    }
del thisdict["model"]

# using clear() method to empty the dictionary
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "color": "red"
    }
thisdict.clear()
print(thisdict)
