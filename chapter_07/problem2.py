# Write a program to great all the person names stored in a list 'l' and which starts with s.
l = ["Supriya","Ashish","Soham","Rahul","Muskan"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")