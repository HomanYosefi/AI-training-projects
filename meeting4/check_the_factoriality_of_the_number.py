number = int(input(" enter number : "))
sycle = 0
for i in range(number):
    sum = 1
    for j in range(1, i):
        sum = sum * j
        
    if sum == number:
        sycle += 1
        print(" yes ")
        break

if sycle == 0:
    print(" no ")