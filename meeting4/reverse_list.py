old_list = []
length_list = int(input(" enter length list : "))

for i in range(length_list):
    number = float(input(f" enter number {i + 1} : "))
    old_list.append(number)

new_list = []
for j in range(length_list - 1, -1, -1):
    new_list.append(old_list[j])  

print(new_list)    