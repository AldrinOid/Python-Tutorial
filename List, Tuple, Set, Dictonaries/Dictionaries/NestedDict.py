# nested the items in dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)
print(myfamily["child2"]["name"])
print(myfamily["child3"]["year"])

# using nested dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print(myfamily["child1"]["name"])
print(myfamily["child2"]["year"])
print(myfamily["child3"]["name"])
print(myfamily["child3"]["year"])
print(len(myfamily))
print(type(myfamily))

# using dict() constructor to create nested dictionary
myfamily = dict(
    child1=dict(name="Emil", year=2004),
    child2=dict(name="Tobias", year=2007),
    child3=dict(name="Linus", year=2011)
)
print(myfamily)
print(myfamily["child2"]["name"])
print(myfamily["child3"]["year"])
print(type(myfamily))

# using for loop to access nested dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
for x, y in myfamily.items():
    print(x, y)
    for i, j in y.items():
        print(i, j)
for x in myfamily:
    print(x)
    for i in myfamily[x]:
        print(i, myfamily[x][i])
for x in myfamily.values():
    print(x)
    for i in x.values():
        print(i)
for x in myfamily.keys():
    print(x)
    for i in myfamily[x].keys():
        print(i)
    