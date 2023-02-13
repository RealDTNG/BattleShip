# Dawson Hoyle 
# Feb 9 2023
# Made to Play Battle Ship alone

import os
import random

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

txts = spots

# "print_brd" prints the board on use of method

def print_brd():
    print(
        f"   A |B |C |D |E  \n1 |{'|'.join(spots[:5])}\n2 |{'|'.join(spots[5:10])}\n3 |{'|'.join(spots[10:15])}\n4 |{'|'.join(spots[15:20])}\n5 |{'|'.join(spots[20:25])}\n{'|'.join(spots[25:30])}")

def txt_write():
    with open('data.txt', 'w') as f:
        f.write(
            f"{'|'.join(txts[:5])}\n{'|'.join(txts[5:10])}\n{'|'.join(txts[10:15])}\n{'|'.join(txts[15:20])}\n{'|'.join(txts[20:25])}\n{'|'.join(txts[25:30])}")

def ai_ship():
    ship1()
    
    def ship1():
        random_ship = f'{random.randrange(0, 24):02}'
        ship1a = random_ship
        if random_ship in '04,09,14,19,24':
            extra_spot = random.randrange(0,3)
            
        
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
    global value_let, value_num, turns
    turns = 0
    value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()
    while value_let not in 'ABCDE':
        print('Please Enter A Valid Column')
        value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()
    value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")
    while value_num not in '12345':
        print('Please Enter A Valid Row')
        value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")   
    turns += 1
    return int(value_num), let_to_num[value_let]

def fire():
    locate = 0
    locate = value_let + (value_num*5-5)    
    if spots[locate] == 'S':
        spots[locate] = 'X'
    elif spots[locate] not in 'XO':
        spots[locate] = 'O'
    else:
        print("ERROR, PLEASE ENTER A EMPTY SPOT")
        turns -= 1
        player_input()