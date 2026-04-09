d = {}   #Empty dictionary
marks = {
    "Supriya": 98,
    "supi": 90,
    "supo":96,
    0: "Supriya"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"supo": 89,"Rita": 79})
# print(marks)

print(marks.get("Supriya2"))  #print none
print(marks["Supriya2"])   #Returns an error