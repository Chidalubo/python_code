year = int(input("enter your date of birth : "))
age = 2021 - year
           
print(age)
if age < 3:
    print("you are an infant")
elif age >= 3 and age <= 12:
    print("you are a child")
elif 13 <= age <= 19 :
    print("you are a teenager ")
elif age <= 59:
    print("you are an adult")
else:
    print("You are an elderly!")
           
           
