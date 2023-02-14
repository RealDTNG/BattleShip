# Dawson Hoyle
# Feb 9 2023
# Made to Play Battle Ship alone

# Import necessary libraries
import os
import random

# Clear the console screen
os.system("cls")

# Initialize variables
hits = 0
run = 34
letters = ["A","B","C","D","E"]
numbers = ["1","2","3","4","5"]
check = ["X ","O "]
txts = []     # list to store board positions
rows = 1       # counter for number of rows in board
menu = True
let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}   # dictionary to map column letters to indices

# Loop through rows to populate spots list with board positions
while rows <= 5:
    txts.append("A" + str(rows))
    txts.append("B" + str(rows))
    txts.append("C" + str(rows))
    txts.append("D" + str(rows))
    txts.append("E" + str(rows))
    rows += 1

spots = txts.copy()    # create a copy of the board

# Define a function to print the board
def print_brd():
    print(f"   A |B |C |D |E  \n1 |{'|'.join(txts[:5])}\n2 |{'|'.join(txts[5:10])}\n3 |{'|'.join(txts[10:15])}\n4 |{'|'.join(txts[15:20])}\n5 |{'|'.join(txts[20:25])}\n{'|'.join(txts[25:30])}")

# Define a function to write the board to a file
def txt_write():
    with open('data.txt', 'w') as f:
        f.write(f"{'|'.join(txts[:5])}\n{'|'.join(txts[5:10])}\n{'|'.join(txts[10:15])}\n{'|'.join(txts[15:20])}\n{'|'.join(txts[20:25])}\n{'|'.join(txts[25:30])}")

# Define a function to place AI ships on the board
def ai_ship():
    def place_ship(length):
        # Pick a random starting position for the ship
        start_pos = random.randint(0, 24)

        # Check if there is enough space to place the ship
        while start_pos + length > 25:
            start_pos = random.randint(0, 24)

        # Check if the selected positions overlap with any existing ships
        for i in range(start_pos, start_pos+length):
            if spots[i] == 'S ':
                # If the positions overlap, start over and try again
                return place_ship(length)

        # If there is enough space and no overlap, place the ship on the board
        for i in range(start_pos, start_pos+length):
            spots[i] = 'S '

    # Place the two ships
    place_ship(2)
    place_ship(2)

# Print game instructions and menu
print(f"Welcome To One Player Battle Ship \nIn This Game Your Goal Is To Battle Against An AI Ship And Try To Sink Its Ship")

# "player_input" takes a txt input from the user to find the spot they want to
def player_input():
    global value_let, value_num, turns
    turns = 0  # Initialize the number of turns to 0
    value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()  # Prompt the user for a column to fire at
    while value_let not in letters:  # If the column entered is not valid, prompt the user again until a valid column is entered
        print('Please Enter A Valid Column')
        value_let = input("Please Pick A Column To Fire At (Ex.. A,B,C...):").upper()
    value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")  # Prompt the user for a row to fire at
    while value_num not in numbers:  # If the row entered is not valid, prompt the user again until a valid row is entered
        print('Please Enter A Valid Row')
        value_num = input("Please Pick A Row To Fire At (Ex.. 1,2,3...):")
    turns += 1  # Increment the number of turns taken by the player
    return int(value_num), let_to_num[value_let]  # Return the row and column as numeric values

def fire():
    global turns, hits  # Use the global variables
    locate = let_to_num[value_let] + (int(value_num) - 1) * 5  # Convert the row and column to a single integer index
    if spots[locate] == 'S ':  # If the player hits a ship
        spots[locate] = 'X '  # Mark the spot as hit
        txts[locate] = 'X '
        print("You've hit an AI ship!")
        hits += 1
        if hits == 4:
            print("YOU WIN!!")
            exit()
    elif spots[locate] not in check:  # If the spot is empty put a miss
        spots[locate] = 'O '  # Mark the spot as missed
        txts[locate] = 'O '
        print("You've missed!")
    else:
        print("ERROR, PLEASE ENTER AN EMPTY SPOT")  # If the spot has already been hit, print an error message
        player_input()  # Ask the player to enter a new spot
    turns -= 1  # Decrement the number of turns taken by the player

# Loop through menu options
while menu:
    cont = input(f"\nType In 'ready' Or 'quit' to Proceed:").lower()
    if cont == "ready":
        ai_ship()
        run = 0
        menu = False
    elif cont == "quit":
        os.system("cls")
        exit()
    else:
        print("ERROR PLEASE ENTER A VALID INPUT")

while run <=10:
    print_brd()
    player_input()
    fire()
    run += 1
