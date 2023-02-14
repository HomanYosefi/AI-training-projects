import random

alphabet_small =['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

alphabet_big = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']

numbers = ['1', '2', '3', '9', '8', '7', '6', '5', '4', '0']

characters = ['-', '_', '@', '#', '$', '*', '(', ')', '+', '!']


while True:
    number = int(input(" enter tedad character ( x > 13 ) : "))
    if number >= 13:
        break

for i in range(number):
    rand = random.randint(1, 4)
    if rand == 1:
        print(random.choice(alphabet_small), end="")

    elif rand == 2:
        print(random.choice(alphabet_big), end="")

    elif rand == 3:
        print(random.choice(numbers), end="")

    elif rand == 4:
        print(random.choice(characters), end="")
