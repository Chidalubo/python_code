questions = ["Which Planets has the most moons",
             "how many continents are there in the World",
             "Who is the first President of Nigeria?"]
answers = ["saturn", "7", "nnamdi azikiwe"]


def question():
    y = 0
    name = input("what is your name?: ")
    print("hello " + name + "," +
          " Welcome to the trivia game where you get to answer some questions.")
    print("Please Note that you only have five trials, after which you will be disqualified and no longer able to continue the game.")
    print("Goodluck!!")
    points = 0
    print("1. ", questions[y])
    user_ans = input("what is your answer?: ").lower()
    if user_ans == answers[y]:
        points += 10
        print("correct!")
        print("Your score = ", points, " points.")
    elif user_ans != answers[y]:
        x = 5
        while x > 1:
            x -= 1
            print("you failed, but you have ", x, " more tries!")
            try1 = input("Try again!: ").lower()
            if try1 == answers[y]:
                print("correct!")
                points += 5
                print(points)
                break
            else:
                if x == 1:
                    print("sorry you failed and you can't continue the game")
                    print("Your final score is = ", points)
                    exit()
    y += 1
    print("2. ", questions[y])
    user_ans = input("what is your answer?: ").lower()
    if user_ans == answers[y]:
        points += 10
        print("correct!")
        print("Your score = ", points, " points.")
    elif user_ans != answers[y]:
        x = 5
        while x > 1:
            x -= 1
            print("you failed, but you have ", x, " more tries!")
            try2 = input("Try again!: ").lower()
            if try2 == answers[y]:
                print("correct!")
                points += 5
                print(points)
                break
            else:
                if x == 1:
                    print("Your final score is =", points)
                    exit()
    y += 1
    print("3. ", questions[y])
    user_ans = input("what is your answer?: ").lower()
    if user_ans == answers[y]:
        points += 10
        print("correct!")
        print("Your score = ", points, " points.")
    elif user_ans != answers[y]:
        x = 5
        while x > 1:
            x -= 1
            print("you failed, but you have ", x, " more tries!")
            try1 = input("Try again!: ").lower()
            if try1 == answers[y]:
                print("correct!")
                points += 5
                print(points)
                break
            else:
                if x == 1:
                    print("sorry you failed and you can't continue the game")
                    print("Your final score is = ", points)
                    exit()
    y += 1


question()
