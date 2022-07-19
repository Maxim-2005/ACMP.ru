N = int(input())
S = V = mS = t = 0

for i in range(N):
	S, V = map(int, input().split())
	if V == 1:
		mS = max(S, mS)
		t = i
print(t - 1)
