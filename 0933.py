A, B, C, T = map(int, input().split())

if T <= A:
    S = B * T
else:
    S = (A * B) + ((T - A) * C)

print(S)
