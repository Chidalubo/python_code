name = input("Please enter yor name contestant: ")
points = 0
question1 = "Which Planets has the most moons"
question2 = "how many continents are there in the World"
question3 = "How many countries are there in Africa"
question4 = "What is the smallest planent in the solar system"
question5 = "How many cm is there in meters"

menu1 = '''

Welcome Contestant ''' + name

print(menu1)

menu2 = '''
THEY ARE FIVE QUESTIONS 

PLEASE PICK FROM NUMBER 1 TO 5.

YOU HAVE 5 TRIES.

DON'T MESS UP (-_-).

WELL GOODLUCK!!!! (^-^)


'''
print(menu2)
pick = int(input("Enter the number: "))


def answer():
    points = 0
    x = 0
    if pick == 1:
        print(question1)
        answer1 = input("What is the answer(^-^): ")
        if answer1 == "saturn":
            print("Correct Kid!")
            points += 10
        else:
            print("You Failed (-_-)")

    elif pick == 2:
        print(question2)
        answer2 = int(input("What is the answer(^-^): "))
        if answer2 == 7:
            print("Correct Kid!")
            points += 10
        else:
            print("You Failed (-_-)")

    elif pick == 3:
        print(question3)
        answer3 = int(input("What is the answer(^-^): "))
        if answer3 == 54:
            print("Correct Kid!")
            points += 10
        else:
            print("You Failed (-_-)")

    elif pick == 4:
        print(question4)
        answer4 = input("What is the answer(^-^): ")
        if answer4 == "pluto":
            print("Correct Kid!")
            points += 10
        else:
            print("You Failed (-_-)")

    elif pick == 5:
        print(question5)
        answer5 = int(input("What is the answer(^-^): "))
        if answer5 == 100:
            print("Correct Kid!")
            points += 10
        else:
            print("You Failed (-_-)")

    print("Your point is", points)


answer()
