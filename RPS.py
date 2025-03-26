import random
while True:
    points = 100
    RPS_game = ["R", "P", "S"]
    comp_input = random.choice(RPS_game)
    menu = '''
    WELCOME TO THE ROCK PAPER SCISSORS

    PLEASE NOTE:
    R - ROCK
    P - PAPER
    S - SCISSORS
    '''

    print(menu)
    user = input("Enter input: ").upper()
    if user == comp_input:
        print("You guessend correctly")
    else:
        points -= 5
        print("try your luck next time")
        print("This was the correct answer", comp_input)
        print(points)
    if points <= 0:
        break
