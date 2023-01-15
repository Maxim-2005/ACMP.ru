arr = []
for i in range(3):
	arr.append(list(input()))
if arr[0][0]  == arr[0][1] == arr[0][2] == "X":
	print("Win")
elif arr[1][0] == arr[1][1] == arr[1][2] == "X":
	print("Win")
elif arr[2][0] == arr[2][1] == arr[2][2] == "X":
	print("Win")
elif arr[0][0] == arr[1][0] == arr[2][0] == "X":
	print("Win")
elif arr[0][1] == arr[1][1] == arr[2][1] == "X":
	print("Win")
elif arr[0][2] == arr[1][2] == arr[2][2] == "X":
	print("Win")
elif arr[0][0] == arr[1][1] == arr[2][2] == "X":
	print("Win")
elif arr[0][2] == arr[1][1] == arr[2][0] == "X":
	print("Win")
elif arr[0][0] == arr[0][1] == arr[0][2] == "O":
	print("Lose")
elif arr[1][0] == arr[1][1] == arr[1][2] == "O":
	print("Lose")
elif arr[2][0] == arr[2][1] == arr[2][2] == "O":
	print("Lose")
elif arr[0][0] == arr[1][0] == arr[2][0] == "O":
	print("Lose")
elif arr[0][1] == arr[1][1] == arr[2][1] == "O":
	print("Lose")	
elif arr[0][2] == arr[1][2] == arr[2][2] == "O" :
	print("Lose")
elif arr[0][0] == arr[1][1] == arr[2][2] == "O":
	print("Lose")
elif arr[0][2] == arr[1][1] == arr[2][0] == "O":
	print("Lose")
else:
	print("Draw")

