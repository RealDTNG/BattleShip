# Dawson Hoyle 
# Feb 9 2023
# Made to Play Battle Ship alone

import os

os.system("cls")

spots = []
rows = 1
menu = True
let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

while rows <= 5:
    spots.append("A" + str(rows))
    spots.append("B" + str(rows))
    spots.append("C" + str(rows))
    spots.append("D" + str(rows))
    spots.append("E" + str(rows))
    rows += 1


# "print_brd" prints the board on use of method


def print_brd():
    print(
        f"   A |B |C |D |E  \n1 |{'|'.join(spots[:5])}\n2 |{'|'.join(spots[5:10])}\n3 |{'|'.join(spots[10:15])}\n4 |{'|'.join(spots[15:20])}\n5 |{'|'.join(spots[20:25])}\n{'|'.join(spots[25:30])}")


def txt_write():
    with open('data.txt', 'w') as f:
        f.write(
            f"{'|'.join(spots[:5])}\n{'|'.join(spots[5:10])}\n{'|'.join(spots[10:15])}\n{'|'.join(spots[15:20])}\n{'|'.join(spots[20:25])}\n{'|'.join(spots[25:30])}")


print(
    f"Welcome To One Player Battle Ship \nIn This Game Your Goal Is To Battle Against An AI Ship And Try To "
    f"Sink Its Ship")

while menu:
    cont = input(f"\nType In 'ready' Or 'quit' to Proceed:").lower()
    if cont == "ready":
        print_brd()
        menu = False
    elif cont == "quit":
        os.system("cls")
        exit()
    else:
        print("ERROR PLEASE ENTER A VALID INPUT")


# "player_input" takes a txt input from the user to find the spot they want to


def player_input():
    value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()
    while value_let not in 'ABCDE':
        print('Please Enter A Valid Column')
        value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()
    value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")
    while value_num not in '12345':
        print('Please Enter A Valid Row')
        value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")
    return int(value_num), let_to_num[value_let]
    locate = 0
    if value_num == 2:
        locate = value_let + 5
    elif value_num == 3:
        locate = value_let + 10
    elif value_num == 4:
        locate = value_let + 15
    elif value_num == 5:
        locate = value_let + 20
    else:
        locate = value_let

