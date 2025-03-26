import random
num = [*range(1, 11)]
print("guess a number from 1 - 10")
user = eval(input("User Input: "))
num2 = random.choice(num)
print("answer:", num2)
if user == num2:
    print("congrats you won.")
elif user != num2:
    x = 3
    while x > 1:
        x -= 1
        try2 = eval(input("try again: "))
        if try2 == num2:
            print("congrats you passed")
            exit()
        else:
            if x == 1:
                print("you failed!")
print("The correct guess is ", num2)
