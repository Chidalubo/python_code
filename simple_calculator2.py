# accept user's input

num1 = input("Enter the first number: ")
num1 = int(num1) # convert to an integer

num2 = input("Enter the second number: ")
num2 = int(num2) # convert to an integer

# display menu
menu = '''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponential
6. Compare
7. Modulo
'''

print("Select an operation you would like to perform on these two numbers:")
print(menu)

choice = input("Enter your number from the menu: ")
choice = int(choice)  # convert the string input to an integer

if choice == 1:
    # add the two numbers
    total = num1 + num2
    print("Your total is: ",total)
elif choice == 2:
    # subtract them
    diff = num1 - num2
    print("The difference between them is: ",diff)
elif choice == 3:
    # multiply them
    product = num1 * num2
    print("The product is: ",product)
elif choice == 4:
    # divide them
    quotient = num1 / num2
    print("The quotient is: ",quotient)
elif choice == 5:
    # find the exponential
    exponential = num1 ** num2
    print("The exponential is: ",exponential)
elif choice == 6:
    # perform a comparism
    greaterThan = num1 > num2
    lessThan = num1 < num2
    equalTo = num1 == num2

    if greaterThan:
        print(num1,"is greater than",num2)
    elif lessThan:
        print(num1,"is less than",num2)
    elif equalTo:
        print(num1, "is equal to",num2)
elif choice == 7:
    # find the modulo
    mod = num1 % num2
    print("The modulo is",mod)
else:
    print("Enter a correct number!")
