# write a program to find the greatest of four number entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# greatest = max(a, b, c, d)
# print(greatest)

if(a>b and a>c and a>d):
    print(a)

elif(b>c and b>d):
    print(b)

elif(c>d):
    print(c)

else:
    print(d)