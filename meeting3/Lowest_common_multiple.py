multiple_1 = []
multiple_2 = []

number_1 = int(input(" enter number 1 : "))
number_2 = int(input(" enter number 2 : "))

sum = 1
cycle = 0
while cycle == 0:
    multiple_1.append(number_1 * sum)
    multiple_2.append(number_2 * sum)
    sum += 1
    for i in range(len(multiple_1)):
        for j in range(len(multiple_2)):
            if multiple_1[i] == multiple_2[j]:
                print(" Lowest common multiple is : ", multiple_1[i])
                cycle = 1

