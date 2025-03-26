import random
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
user = int(input("User Input: "))
num2 = random.choice(num)
if user == num2:
    print("congrats you won.")
elif user != num2:
    x = 3
    while x > 1:
        x -= 1
        try2 = int(input("try again: "))
        if try2 == num2:
            print("congrats you passed")
            exit()
        else:
            if x == 1:
                print("you failed!")
print("The correct guess is ", num2)
