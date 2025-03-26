y = input("Please enter a word: ")
z = 0
v = 0
while z < len(y):
    if y[z] == "a":
        v += 1
    if y[z] == "e":
        v += 1
    if y[z] == "i":
        v += 1
    if y[z] == "o":
        v += 1
    if y[z] == "u":
        v += 1
print(v)
