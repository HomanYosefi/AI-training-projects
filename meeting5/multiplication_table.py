multiplication_table = []
list_help = []

n = int(input(" enter number n : "))
m = int(input(" enter number m : "))

for i in range(1, n):
    for j in range(1, m):
        list_help.append(i * j)

    multiplication_table.append(list_help)
    list_help = []


for zarb in multiplication_table:
    print(zarb)        