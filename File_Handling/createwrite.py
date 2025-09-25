# append a text to an existing file
with open("demofile.txt", "a") as f:
    f.write(" I love coding in python!")

# checking if the added content is visible inside the file
with open("demofile.txt") as f:
    print(f.read())

# write or overwrite the content of the text
with open("demofile.txt", "w") as f:
    f.write(" I love coding in python!")

# checking if the added content is visible inside the file
with open("demofile.txt") as f:
    print(f.read())

f.close()

# create new file. returns an error if that file is already existing
# f = open("demonewfile.txt", "x")

with open ("demonewfile.txt", "w") as f:
    f.write("I love solving problem using python!")

with open("demonewfile.txt", "a") as f:
    f.write(" Let's learn python!")

f = open("demonewfile.txt")
print(f.read())

f.close()



