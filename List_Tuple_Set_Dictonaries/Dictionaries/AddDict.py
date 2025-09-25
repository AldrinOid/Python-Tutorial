# adding items in the dictionary
thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# using update() method to add item
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
thisdict.update({"color": "red"})
print(thisdict)
