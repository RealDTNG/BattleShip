# Dawson Hoyle 
# Feb 9 2023
# Made to Play Battle Ship alone

import os

os.system("cls")

spots = []
rows = 1
menu = True
while rows <= 5:
    spots.append("A" + str(rows))
    spots.append("B" + str(rows))
    spots.append("C" + str(rows))
    spots.append("D" + str(rows))
    spots.append("E" + str(rows))
    rows += 1


def print_brd():
    print(
        f"{'|'.join(spots[:5])}\n{'|'.join(spots[5:10])}\n{'|'.join(spots[10:15])}\n{'|'.join(spots[15:20])}\n{'|'.join(spots[20:25])}\n{'|'.join(spots[25:30])}")


with open('data.txt', 'w') as f:
    f.write(
        f"{'|'.join(spots[:5])}\n{'|'.join(spots[5:10])}\n{'|'.join(spots[10:15])}\n{'|'.join(spots[15:20])}\n{'|'.join(spots[20:25])}\n{'|'.join(spots[25:30])}")

print(
    f"Welcome To One Player Battle Ship \nIn This Game Your Goal Is To Battle Against A AI Ship As You Both Try To "
    f"Sink Each-others Ship")

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


def player_input():
    value = input("Please Pick A Spot To Fire At:")
