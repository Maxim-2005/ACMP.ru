N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
	arrC = []
	arrNC = []
	for j in range(len(arr)):
		if arr[j] % 2 == 0:
			arrC.append(arr[j])
		else:
			arrNC.append(arr[j])
print(*arrNC)
print(*arrC)
if len(arrC) >= len(arrNC):
	print("YES")
else:
	print("NO")
	
	
