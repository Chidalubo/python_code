from question_answer import questions, answers


def question(a, b):
    y = 0
    name = input("what is your name?: ")
    print("hello " + name + "," +
          " Welcome to the trivia game where you get to answer some questions.")
    print("Please Note that you only have five trials, after which you will be disqualified and no longer able to continue the game.")
    print("Goodluck!!")
    points = 0
    while y < len(a):
        print(a[y])
        user_ans = input("what is your answer?: ").lower()
        if user_ans == b[y]:
            points += 10
            print("CORRECT!")
            print("Your score = ", points, " points.")
        elif user_ans != b[y]:
            x = 5
            while x > 1:
                x -= 1
                print("you failed, but you have ", x, " more tries!")
                try1 = input("Try again!: ").lower()
                if try1 == b[y]:
                    print("correct!")
                    points += 5
                    print(points)
                    break
                else:
                    if x == 1:
                        print("YOU ARE DUMB (-_-)")
                        print("Your final score is = ", points, "points.")
                        exit()
        y += 1


question(questions, answers)
