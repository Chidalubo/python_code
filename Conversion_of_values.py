
def convert1():
    print("Conversion from cm to In")
    cm = float(input("How mant centimeters do you want to convert Inches: "))
    result = cm * 0.394
    print(cm, "cm is equal to", result, "inches")


def convert2():
    print("Conversion from kg to pounds")
    kg = float(input("How mant Kg do you want to convert pounds: "))
    result = kg * 2.205
    print(kg, "kg is equal to", result, "lbs")


menu = '''
CONVERSION OF VALUES

1. Conversion from cm to In
2. Conversion from kg to pounds
'''
print(menu)
num = int(input("Pick what you want to convert: "))

if num == 1:
    convert1()

elif num == 2:
    convert2()

else:
    print("INVALID!!")
