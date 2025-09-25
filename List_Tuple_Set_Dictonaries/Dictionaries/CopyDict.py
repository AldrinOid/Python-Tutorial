# copy the items of one dictionary to another dictionary
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
mydict = thisdict.copy()    
print(mydict)

# using dict() method to copy dictionary
thisdict = {
    "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
mydict = dict(thisdict) 
print(mydict)

