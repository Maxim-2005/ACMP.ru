n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for i in range(m):
	a, b = map(int, input().split())
	arrTemp = []
	for j in range(a-1, b):
		arrTemp.append(arr[j]);
	print(*arrTemp)
