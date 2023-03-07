import pyfiglet
import random
from os import _exit
import termcolor
import time

start_time = time.time()
title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_boord = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]


def show():
    for cell in game_boord:
        for j in cell:
            if j == "O":
                print(termcolor.colored(j ,color="blue"), end=" ")

            elif j == "X":    
                print(termcolor.colored(j, color="red"), end=" ")

            else :
                print(j, end=" ")

        print() 


def full():
    sum = 0
    for cell in game_boord:
        for j in cell:
            if j == "-":
                sum += 1

    if sum == 0:
        return 1

    else :                      
        return 0            


def check_win():
    for i in range(3):
        sum_x = 0
        sum_o = 0
        for j in range(3):
            if game_boord[i][j] == "X":
                sum_x += 1
            elif game_boord[i][j] == "O":
                sum_o += 1

        if sum_x == 3:
            print(" player 1 win 🎉🎉🎉")   
            exit()    
        elif sum_o == 3:
            print(" player 2 win 🎉🎉🎉")
            exit()

    for i in range(3):
        sum_x = 0
        sum_o = 0
        for j in range(3):
            if game_boord[j][i] == "X":
                sum_x += 1
            elif game_boord[j][i] == "O":
                sum_o += 1

        if sum_x == 3:
            print(" player 1 win 🎉🎉🎉")   
            exit()    
        elif sum_o == 3:
            print(" player 2 win 🎉🎉🎉")
            exit() 

    sum_x = 0
    sum_o = 0

    for i in range(3):
        if game_boord[i][i] == "X":
            sum_x += 1
        elif game_boord[j][i] == "O":
            sum_o += 1

    if sum_x == 3:
            print(" player 1 win 🎉🎉🎉")
            exit()
    elif sum_o == 3:
        print(" player 2 win 🎉🎉🎉")
        exit() 
        




print(" [1]-- two player game \n [2]-- computer games")         
select_player = int(input(" enter number list : "))

if select_player == 1:
    show()
    while True:
        print(" player 1 : ")
        while True:
            row = int(input(" row : "))
            col = int(input(" col : "))
            row -= 1
            col -= 1

            if game_boord[row][col] == "-":
                if 0 <= row <= 2 and 0 <= col <= 2:
                    game_boord[row][col] = "X"
                    break
                else :
                    print(" lotfan dorost vared konid :| ")

            else :
                print(" khone morede nazar por ast :/")

        show()
        check_win()
        ful = full()
        if ful == 1:
            print(" finish game ")
            break
        print(" player 2 : ")
        while True:
            row = int(input(" row : "))
            col = int(input(" col : "))
            row -= 1
            col -= 1

            if game_boord[row][col] == "-":
                if 0 <= row <= 2 and 0 <= col <= 2:
                    game_boord[row][col] = "O"
                    break      
                else:
                    print(" lotfan dorost vared konid :| ")

            else:
                print(" khone morede nazar por ast :/")
        show()
        check_win()
        ful = full()
        if ful == 1:
            print(" finish game ")
            break

elif select_player == 2:
    show()
    while True:
        print(" player 1 : ")
        while True:
            row = int(input(" row : "))
            col = int(input(" col : "))
            row -= 1
            col -= 1

            if game_boord[row][col] == "-":
                if 0 <= row <= 2 and 0 <= col <= 2:
                    game_boord[row][col] = "X"
                    break
                else:
                    print(" lotfan dorost vared konid :| ")

            else:
                print(" khone morede nazar por ast :/")

        show()
        check_win()
        ful = full()
        if ful == 1:
            print(" finish game ")
            break
        print(" player pc : ")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if game_boord[row][col] == "-":
                if 0 <= row <= 2 and 0 <= col <= 2:
                    game_boord[row][col] = "O"
                    break
        show()
        check_win()
        ful = full()
        if ful == 1:
            print(" finish game ")
            break



else :
    print(" to list nadarim dobare deghat kon ")

finish = time.time()

hour = 0
min = 0
sec = int(finish - start_time)

if sec >= 3600:
    hour = sec/3600
    sec = sec % 3600
    if sec > 60:
        min = sec/60
        sec = sec % 60

elif sec < 3600:
    min = sec/60
    sec = sec % 60

print("\ntime is: ", int(hour), ":", int(min), ":", sec)
