import random
RPS_game = ["R", "P", "S"]
i = 0
while i < 10:
    comp = random.choice(RPS_game)
    print(comp)
    i += 1
