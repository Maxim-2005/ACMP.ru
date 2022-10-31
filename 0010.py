A, B, C, D = map(int, input().split())
arr = []

for i in range(-101, 101):
	if A * i * i * i + B * i * i + C * i + D == 0: 
		arr.append(i);

arr.sort()
print(*arr)
