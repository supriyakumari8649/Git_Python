# Write a program to find the sum of first n natural number using while loop.
num = int(input("Enter natural number: "))
i = 0
sum = 0
while(i<=num):
    sum += i
    i += 1
   
print("sum is",sum)