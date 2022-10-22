N = int(input())
x = 0
t = 0

arr = list(map(int, input().split()))
arr.append(arr[0])
arr.append(arr[1])

for i in range(N):
	x = arr[i-1] + arr[i] + arr[i+1]
	t = max(t, x)

print(t)
