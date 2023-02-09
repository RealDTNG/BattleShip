# Dawson Hoyle 
# Feb 9 2023
# Made to Play Battle Ship alone

import os
os.system("cls")

spots = []
rows = 1

while rows <= 5:
    spots.append("A" + str(rows))
    spots.append("B" + str(rows))
    spots.append("C" + str(rows))
    spots.append("D" + str(rows))
    spots.append("E" + str(rows))
    rows += 1

print(f"{spots[:5]} \n\n{spots[5:10]} \n\n{spots[10:15]} \n\n{spots[15:20]} \n\n{spots[20:25]} \n\n{spots[25:30]}")