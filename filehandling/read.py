# open and read demofile.txt
f = open("demofile.txt") # you input here also the location path of the file 
print(f.read())

# reading only specify characters inside the file
f = open("demofile.txt") # you input here also the location path of the file 
print(f.read(5))

# using readline statement, returns the first line of the content of the file and leave next line
f = open("demofile.txt") # you input here also the location path of the file 
print(f.readline())

# using with statement
with open("demofile.txt") as f:
    print(f.read())

# you can do looping to print the content of the file
with open("demofile.txt") as f:
    for x in f:
        print(x)

# best practice, always close the file that you opened
f = open("demofile.txt") # you input here also the location path of the file 
print(f.read())
f.close()