import random

while True:
    user_response = int(input("Enter the number one and we will roll the dice for you : "))
    if user_response == 1:
        dice = random.randint(1, 6)
        print(" dice number is : ", dice)
        if dice == 6:
            print("Hooray, your dice number is equal to six, so as a bonus, you have the right to throw the dice again")
        elif dice != 6:
            break
    