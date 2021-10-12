C, H, O = map(int, input().split())

C = C // 2
H = H // 6
O = O // 1

if C < H and C < O:
	print(C)
elif H < C and H < O:
	print(H)
else:
	print(O)