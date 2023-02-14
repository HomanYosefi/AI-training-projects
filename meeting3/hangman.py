import random

True_list = []
False_list = []

library_name = ["Install", "latest", "PowerShell",
                "features", "improvements Copyright", "Microsoft", "Corporation", "number", "NITRO", "directory", "meeting"]

name = random.choice(library_name)
name = name.lower()

for i in range(len(name)):
    if name[i] == " ":
        print(end="  ")
    else:    
        print("_", end=" ")


while len(False_list) != 6:
    char_name = input(" enter charactr : ")
    char_name = char_name.lower()
    win = 0
    if len(char_name) == 1:
        if char_name in name:
            True_list.append(char_name)
        else:
            False_list.append(char_name)

        for i in range(len(name)):
            if name[i] == " ":
               print(end="  ")
            elif name[i] in True_list:
                print(name[i], end=" ")
            else:
                print("_", end=" ")
                win += 1

        if win == 0:
            break    

    else: 
        print(" please enter a character ")

if len(False_list) == 6:
    print(" game over ")

elif win == 0:
    print(" you win 🎉🎉🎉")