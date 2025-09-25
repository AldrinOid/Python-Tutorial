# remove or delete the file
import os

# os.remove("deletefile.txt")

if os.path.exists("deletefile.txt"): 
    os.remove("deletefile.txt")
else:
    print("the file is already deleted")