# A spam comment is defined as a text containing following keywords: "Make a lot of money","buy now","Subscribe this","Click this".Write a program to detect these spams.

comment = input("Enter your comment: ")

if("Make a lot of money" in comment or
    "Buy now" in comment or 
    "Subscribe this" in comment or 
    "Click this" in comment):
    print("Thise is a spam comment")

else:
    print("Thise is a not spam comment")