birth_year = int(input("Please enter your year of birth: "))
age = 2021 - birth_year
print(age)
if age <= 3:
    print("Boy you are an infant how can you use this!!!!!")
elif age <= 12:
    print("go and sleep child")
elif age <= 19:
    print("Yo teen!!")
elif age <= 59:
    print("Good day adult")
elif age >= 60:
    print("Good day sensi")
