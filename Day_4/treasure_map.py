row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1 #define column position
row = int(position[1]) - 1 #define row position

map[row][col] = "X" #put treasure at specified position

print(f"{row1}\n{row2}\n{row3}")