# write a program to fill in a letter template given below whit name and date.
# name = input("Enter your name: ")
# date = input("Enter your date: ")
# letter = f"""
# Dear {name},
# you are selected!
# Date: {date}"""
# print(letter)

letter = '''
Dear <|name|>,
you are selected!
Date: <|date|>'''
print(letter.replace("<|name|>","Supriya").replace("<|date|>","28-03-2026"))