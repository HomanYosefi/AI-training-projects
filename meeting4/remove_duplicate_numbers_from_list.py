one_list = []

length_list = int(input(" enter length list : "))

for i in range(length_list):
    number = float(input(f" enter number {i + 1} : "))
    one_list.append(number)

new_list = []
for num in one_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)        