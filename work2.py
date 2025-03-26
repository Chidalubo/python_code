list1 = [1, 3, 4, 7, 87, 46, 8, 34, 7]


def max45(num):
    highest = 0
    x = 0
    while x < len(num):
        if num[x] > highest:
            highest = num[x]
        x += 1
    return highest


print(max45(list1))
