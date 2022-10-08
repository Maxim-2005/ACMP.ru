n = int(input())
arr = list(map(int, input().split()))
k = int(input())
t = 0

for i in arr:
	t += min(i, k)
print(t)
