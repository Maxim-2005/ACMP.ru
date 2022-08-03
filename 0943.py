N, M, Y, X = map(int, input().split());
S = M * Y;

if Y % 2 == 0:
	print(S - X)
else:
	print((S - (M - X)) - 1)s
