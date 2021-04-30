# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print(f"this is map : {map}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

columnIndex = int(str(position[0]))
rowIndex = int(str(position[1]))
#Map stores the nested list so "[rowIndex-1]" we slect the row and "[columnIndex-1]" we select coloumn and assign value "X" to it.
map[rowIndex-1][columnIndex-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")