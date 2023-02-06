import random

number = random.randint(0, 100)
number_of_guesses = 1

while True: 
    karbar_number = int(input(" enter number : "))
    if karbar_number > number:
        print(" choose a lower number ")
        number_of_guesses += 1
        

    if karbar_number < number:
        print(" choose a higher number ")
        number_of_guesses += 1

    if karbar_number == number:
        print(" your guess was right 🎉🎉🎉")
        break        

print(" the number of your guess is equal to : ", number_of_guesses)    