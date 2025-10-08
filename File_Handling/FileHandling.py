file = open("TestFile.txt", "r")
content = file.readlines()
print(content)
file.close()


with open ("newfile.txt", "w") as newfile:
    newfile.write("This is a new file created using the 'with' statement.\n")
    newfile.write("It automatically handles file closing.")
     