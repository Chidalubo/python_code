name = input("Please enter yor name contestant: ")
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
    x =
    points = 0

    if pick == 1:
        print(question1)
        answer1 = input("What is the answer(^-^): ")
        if answer1 == "saturn":
                print("Correct Kid!")
                points += 10
            else:
                if answer1 != "saturn":

                    x -= 1


