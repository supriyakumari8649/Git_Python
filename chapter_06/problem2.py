# write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. assuma 3 subject and take marks as an input for the user.

m1 = int(input("Enter first marks: "))
m2 = int(input("Enter second marks: "))
m3 = int(input("Enter third marks: "))

percentage = (m1+m2+m3)/3

if(percentage>=40 and (m1>=33 and m2>=33 and m3>=33)):
    print("pass")

else:
    print("fail")
