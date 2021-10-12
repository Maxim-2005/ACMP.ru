N = int(input())
S = 0
O = 0

for i in range(N):
    m = int(input())
    S += m
O = N - S
if S > O:
    print(O)
else:
    print(S)
