n, a, b = map(int, input().split())
for i in range(n-1):
	a, b = (b - a), a
print(a, b)
