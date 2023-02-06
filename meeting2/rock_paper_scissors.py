import random

rounds = int(input(" enter rounds : "))
star_pc = 0
star_user = 0

for i in range(rounds):
    user_selection = input(" Rock, paper and scissors ? ")
    pc_random = random.randint(1, 3)
    if pc_random == 1:
        pc_selection = "rock"

    elif pc_random == 2:
        pc_selection = "paper"

    elif pc_random == 3:
        pc_selection = "scissors"

    print(" pc selected : ", pc_selection)    

    if pc_selection == user_selection:
        print(" In this hand, you and the computer are equal")

    elif (pc_selection == "rock" and user_selection == "paper") or (pc_selection == "scissors" and user_selection == "rock") or (pc_selection == "paper" and user_selection == "scissors"):
        star_user += 1
        print(" A point was added for the user") 

    elif (user_selection == "rock" and pc_selection == "paper") or (user_selection == "scissors" and pc_selection == "rock") or (user_selection == "paper" and pc_selection == "scissors"):
        star_pc += 1
        print(" A point was added for the pc")     
        
if star_user > star_pc: 
    print(" user win 🎉🎉🎉") 

elif star_user < star_pc: 
    print(" pc win 🎉🎉🎉")  

elif star_pc == star_user: 
    print(" pc and user win 🎉🎉🎉")
