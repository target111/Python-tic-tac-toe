# -*- coding: utf-8 -*-

import sys,os,random
from time import sleep

turn=["X", "O"]

type=["1","2","3","4","5","6","7","8","9"]

def table():

    os.system("clear")
    print(" "*25+type[0]+"|"+type[1]+"|"+type[2])
    print(" "*25+"------")
    print(" "*25+type[3]+"|"+type[4]+"|"+type[5])
    print(" "*25+"------")
    print(" "*25+type[6]+"|"+type[7]+"|"+type[8])

def pos(weapon, position):
    position=int(position)-1

    if type[position] in turn:
       pass

    else:
       type[position] = str(weapon)

def user_input():
    temp_position = input("\nWhat is your next move? (1-9)")
    try:
        if int(temp_position) in range(1,10):
            global position_x
            position_x = temp_position
        else:
            print("Please choose a number within 1-9")
            sleep(2)
    except:
        print("Please pass an integer")
        sleep(2)

def win():
    if type[0] == type[1] == type[2] and type[0] in turn and type[1] in turn and type[2] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[3] == type[4] == type[5] and type[3] in turn and type[4] in turn and type[5] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[6] == type[7] == type[8] and type[6] in turn and type[7] in turn and type[8] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[0] == type[4] == type[8] and type[0] in turn and type[4] in turn and type[8] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[2] == type[4] == type[6] and type[2] in turn and type[4] in turn and type[6] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[2] == type[5] == type[8] and type[2] in turn and type[5] in turn and type[8] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    elif type[0] == type[3] == type[6] and type[0] in turn and type[3] in turn and type[6] in turn:
        table()
        print(current_turn + " won!")
        sleep(2)
        sys.exit()

    squares_used = 0
    for i in type:
        if i == "X" or i == "O":
            squares_used = squares_used + 1

    if squares_used == 9:
        table()
        print("It's a draw!")
        sleep(2)
        sys.exit()

def main():
    while True:

        global current_turn

        for current_turn in turn:
            table()
            user_input()
            pos(current_turn, position_x)
            win()

if __name__ == "__main__":
    main()
