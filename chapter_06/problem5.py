# write a program which finds out whether a given name is present in a list or not
names = ["Supriya","Ashish","Divya","Rohan","Muskan","Rushan"]

name = input("Enter a name: ")

if (name in names):
    print("Name is present")
else:
    print("Name is not present")