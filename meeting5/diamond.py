number = int(input(" enter number : "))
space = number 

for i in range(number):
    for s in range(space):
        print(end= " ")

    space -= 1
    for star in range(number - space):
        print("*", end= "")

    for d in range(i):
        print("*", end= "")    

    print()

space += 2

for e in range(number - 1):
    for sp in range(space):
        print(end=" ")

    space += 1
    for stars in range(number - space + 2):
        print("*", end="")

    for d in range(number - space + 1):
        print("*", end="")

    print()
