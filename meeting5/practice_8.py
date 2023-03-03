n = int(input(" enter number n : "))
m = int(input(" enter number m : "))

for i in range(n):
    print()
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                print("#", end="")

            else :
                print("*", end="")  

        else :
            if j % 2 == 0:
                print("*", end="")

            else:
                print("#", end="")
