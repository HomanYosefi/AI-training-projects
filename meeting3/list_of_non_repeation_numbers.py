import random

list = []

number = int(input(" enter number : "))
help_box = 0

while number != help_box:
    x = random.randint(0, (number - 1) * 2)
    if x not in list:
        list.append(x)
        help_box += 1

print(list)    
    


