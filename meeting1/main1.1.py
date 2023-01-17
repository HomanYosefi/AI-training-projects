import math

# print(math.sin(math.radians(30)))

while True :
    print("\n\n\n[1]-- + \n[2]-- -\n[3]-- / \n[4]-- * \n[5]-- jazr(radical)\n[6]-- sin zavieh\n[7]-- cos zavieh \n[8]-- cot zavieh \n[9]-- tan zavieh ")
    print("[10]-- factorial\n[11]-- exit")
    esk = int(input("\n\n enter number list : "))


    if esk == 1:
        number1 = float(input(" enter number 1 : "))
        number2 = float(input(" enter number 2 : "))
        print(number1, " + ", number2, " = ", number1 + number2)


    elif esk == 2:
        number1 = float(input(" enter number 1 : "))
        number2 = float(input(" enter number 2 : "))
        print(number1, " - ", number2, " = ", number1 - number2)


    elif esk == 3:
        number1 = float(input(" enter number 1 : "))
        number2 = float(input(" enter number 2 : "))
        print(number1, " / ", number2, " = ", number1 / number2)


    elif esk == 4:
        number1 = float(input(" enter number 1 : "))
        number2 = float(input(" enter number 2 : "))
        print(number1, " * ", number2, " = ", number1 * number2)

    elif esk == 5:
        number = int(input(" enter number to jazr : "))
        print(math.sqrt(number))

    elif esk == 6:
        number = int(input(" enter number to sin : "))
        print(math.sin(math.radians(number)))

    elif esk == 7:
        number = int(input(" enter number to cos : "))
        print(math.cos(math.radians(number)))

    elif esk == 8:
        number = int(input(" enter number to cot : "))
        print(math.cos(math.radians(number)) / math.sin(math.radians(number)))

    elif esk == 9:
        number = int(input(" enter number to tan : "))
        print(math.tan(math.radians(number)))


    elif esk == 10:
        number = int(input(" enter number to faktoriel : "))
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i
        print(fact)


    elif esk == 11:
        break
