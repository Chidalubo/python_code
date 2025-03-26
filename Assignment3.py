bank_details = {
    "Brayant.O": 100000000000,
    "Andrea.Y": 12354650,
    "Anselm.A": 123000,
    "Ugo.P": 1345096,
    "Romeo.A": 1235608534,
    "Valerie.R": 14579784
}


def View_Bank():
    for char in bank_details:
        print(char, ":", bank_details[char])


def Add_Account():
    print("PLEASE WRITE THE ACCOUNT NAME IN THIS FORMAT John.D, John is the first name and D is the first letter of the surname")
    View_Bank()
    account_name = input("Please enter the account name: ")
    account_amount = int(input("Please enter the amount of cash: "))
    bank_details[account_name] = account_amount
    View_Bank()


def Amount_Check():
    View_Bank()
    check = input("Please enter the Account Name you want to check: ")
    print("The ammount has is ", check, " is ", bank_details[check])


def Delete_Account():
    View_Bank()
    del_account = input(
        "Please write the name of the account you want to delete: ")
    bank_details.pop(del_account)
    View_Bank()


menu = '''
WELCOME PLEASE PICK AN OPTION:

1.) VIEW ALL BANK ACCOUNTS
2.) ADD A NEW BANK ACCOUNT
3.) CHECK AMOUNT OF A PARTICULAR BANK ACCOUNT
4.) DELETE AN ACCOUNT
'''
while True:
    print(menu)

    num = int(input("PLease enter the option: "))

    if num == 1:
        View_Bank()

    elif num == 2:
        Add_Account()

    elif num == 3:
        Amount_Check()

    elif num == 4:
        Delete_Account()

    else:
        print("INVALID")

    continue1 = input("DO YOU WANT TO CONTINUE (Y/N): ")
    if continue1 == "Y":
        continue

    else:
        print("Thnak you for your time kind")
        break
