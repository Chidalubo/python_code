time = int(input("Please enter the time: "))

if time >= 0 and time < 13:
    print("Good Morning")

elif time > 12 and time < 17:
    print("Good Afternoon")

elif time > 16 and time < 21:
    print("Good Evening")

elif time > 20 and time < 24:
    print("Good Night")

else:
    print("Wrong Input")
