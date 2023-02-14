while True:
    number = int(input(" enter number : "))
    if number >= 0:
        break
    else:
        print(" the entered number must be greater than 0 ")

for i in range(number):
    if i % 2 == 0:
        print("*", end= "")
    else:
        print("#", end= "")    
