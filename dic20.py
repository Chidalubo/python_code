from dic2 import quiz

for key in quiz:
    print(quiz[key]["question"])
    user = input("What is the answer: ").lower()
    if quiz[key]["answer"].lower() == user:
        print("Hurray")
