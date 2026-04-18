# Write a python function to remove a given word from a list ad strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item)
    return n

l = ["Supriya","Ashish","Subham","Rohan","as"]
print(rem(l, "Rohan"))