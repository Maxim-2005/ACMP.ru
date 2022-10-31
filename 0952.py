n, m = map(int, input().split())

if n == 0 and m > 0:
	print("Impossible")
elif m == 0:
	print(n, n)
else:
	minS = (max(n, m))
	maxS = (n + m - 1)
	print(minS, maxS)
