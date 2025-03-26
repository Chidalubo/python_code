
Students = ["John", "Angel", "Adam", "Paul"]


def see_students():
    for names in Students:
        print(".", names)


def new_students():
    new_name = input("Please enter the name of the new student: ")
    Students.append(new_name)
    see_students()


def delete_students():
    see_students()
    delete_name = input(
        "Please enter the name of the student you want to delete: ")
    if delete_name in Students:
        Students.remove(delete_name)
        see_students()
    else:
        print('NAME NOT FOUND IN THE LIST')


menu = '''
SCHOOL ADMIN PANEL

1. See Students inside
2. Add a new student
3. Remove a students
'''
while True:
    print(menu)
    num = int(input("Pick which function to use: "))
    if num == 1:
        see_students()

    elif num == 2:
        new_students()

    elif num == 3:
        delete_students()

    else:
        print("INVALID!!")

    continue1 = input("Do you want to continue (Y/N): ")
    if continue1 == 'Y':
        continue
    else:
        break
