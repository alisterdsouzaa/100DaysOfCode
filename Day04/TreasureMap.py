# Nested List in Python

row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]

treasurership = [row1, row2, row3]

print(f"{row1}\n{row2}\n,{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0] )
vertical = int(position[1])

treasurership[vertical-1][horizontal-1] = "O"

print(f"{row1}\n{row2}\n,{row3}")
