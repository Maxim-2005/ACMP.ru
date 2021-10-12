A = input()
B = 0
C = 0
D = 0
E = 0

A = int(A)
B = int(B)
C = int(C)
D = int(D)
E = int(E)

B = A // 1000
C = A // 100 % 10
D = A // 10 % 10
E = A % 10

if(B == E and C == D):
	print('YES')
else:
	print('NO')
