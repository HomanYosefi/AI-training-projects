from math import factorial
list_khayam = []
box = []

number = int(input(" enter number : "))

for i in range(number):
    for j in range(i + 1):
        box.append(factorial(i) // (factorial(j) * factorial(i - j)))

    list_khayam.append(box)
    box =[]

for l in list_khayam:
    print(l)