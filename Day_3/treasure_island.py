# https://ascii.co.uk/art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? L (left) or R (right)? ")

if direction == "R":
    print("Fall into a hole.\nGame over.")
elif direction == "L":
    ride = input("Do you want to swim (S) or wait for a boat (B)? ")
    if ride == "S":
        print("Attacked by trout.\nGame over.")
    elif ride == "B":
         door = input("Welcome to the island! Which door would you like open? R (red), B (blue) or yellow (Y)? ")
         if door == "Y":
             print("You Win!")
         elif door == "R":
             print("Burned by fire.\nGame over.")
         elif door == "B":
             print("Eaten by beasts.\nGame over.")
         else:
             print("You have entered a wrong value! Game over.")            
    else:
        print("You have entered a wrong value!")
else:
    print("You have entered a wrong value.")