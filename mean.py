list12 = [1, 3, 45, 4, 6, 7, 8, 5, 45]


def sum1(x):
    sum2 = 0
    for i in x:
        sum2 = sum2 + i

    mean = sum2 / len(x)

    return mean


print(sum1(list12))
