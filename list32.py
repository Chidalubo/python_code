num = [10, 2, 34, 4, 5]
p = 0
d = 0
f = 0
for y in num:
    if y > 0:
        p += 1
print(p)

for z in num:
    if z < 0:
        d += 1
print(d)

for x in num:
    f = x + f
print(f)
