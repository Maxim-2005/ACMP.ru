N = int(input())
res = maxVoz = -1

for i in range(N):
	V, S = map(int, input().split())
	if S == 1 and V > maxVoz:
		maxVoz = V 
		res = i + 1
print(res)
