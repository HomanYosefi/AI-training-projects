

my_list = []
truu = 0
number_list  = int(input(" enter the length of the list : "))
for i in range(number_list):
    number = float(input(" enter number : "))
    my_list.append(number)

for i in range(number_list):
    for j in range(number_list - 1):
            if my_list[j] > my_list[j + 1]:
                truu += 1
                help_box = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = help_box


if truu == 0:
    print(" your list numbers were in order")
else:
    print(" the numbers in your list were not in order, bot the program wrote the numbers in your list in order : ", my_list)



