name_lists = {}


def greeting():
    name = input("Please input your name: ")
    greeting = "Good day " + name + "."
    return greeting


def show():
    for i in name_lists:
        print(i, " ", name_lists[i])


def store(name_list):
    name = input("Please input your name: ")
    name1 = input("Please input your name: ")
    name2 = input("Please input your name: ")
    name3 = input("Please input your name: ")
    name4 = input("Please input your name: ")
    name_list = [name, name1, name3, name4, name2]


print(store(name_lists))
