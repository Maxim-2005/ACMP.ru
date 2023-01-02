m, n, i, j, c = map(int, input().split())

if (m * n) % 2 == 0:
	print("equal")
elif (i + j) % 2 == 0 and c == 1:
	print("white")
elif (i + j) % 2 == 0 and c == 0:
	print("black")
elif (i + j) % 2 != 0 and c == 1:
	print("black")
elif (i + j) % 2 != 0 and c == 0:
	print("white")
