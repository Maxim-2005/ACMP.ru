A, B, C = map(int, input().split())

if (A + B == C) or (A + C == B) or (B + C == A):
	print('YES')
else:
	print('NO')