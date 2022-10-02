N = int(input())
arrB = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
arrN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(N):
	s =  input()
	if len(s) == 6 and s[0] in arrB and s[4] in arrB and s[5] in arrB and s[1] in arrN and s[2] in arrN and s[3] in arrN:
		print('Yes')
	else:
		print('No')
