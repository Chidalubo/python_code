# accept input from user
num1 = input("Enter the first number: ")
num1 = int(num1)
num2 = input("Enter the second number: ")
num2 = int(num2)
# display menu
menu = '''
1. Add
2. Substract
3. Multiply
4. divide
5. Exponetial
6. Compare
'''

print("Select an operation you would like to perform on these two numbers: ")
print(menu)

choice = input("Enter your choice: ")
choice = int(choice)
if choice == 1:
    # add the two numbers
    total = num1+num2
    print("Your total is: ", total)
elif choice == 2:
    diff = num1-num2
    print("Your total is: ", diff)
elif choice == 3:
    total3 = num1*num2
    print("Your total is: ", total3)
elif choice == 4:
    total4 = num1/num2
    print("Your total is: ", total4)
elif choice == 5:
    total5 = num1**num2
    print("Your total is: ", total5)
