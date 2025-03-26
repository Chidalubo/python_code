questions = "Which Planets has the most moons"
questions2 = "how many continents are there in the World"
answers1 = "saturn"
answer2 = "7"


def question():
    name = input("what is your name?: ")
    print("hello " + name)
    i = 0
    points = 0
    print(questions)
    user_ans1 = input("what is your answer?: ")
    if user_ans1 == answers1:
        points += 10
        print("correct!")
        print("Your score = ", points, " points.")
    elif user_ans1 != answers1:
        x = 5
        while x > 1:
            x -= 1
            print("you failed, but you have ", x, " more tries!")
            try1 = input("Try again!: ")
            if try1 == answers1:
                print("correct!")
                points += 10
                print(points)
                break
            else:
                if try1 != answers1:
                    print(
                        "you failed and you can't continue, but thank you for your time")


question()
