N = int(input())
X = 1
res = ('NO')

while N >= X:
	if X == N:
		res = ('YES')
		break
	X *= 2
print(res)