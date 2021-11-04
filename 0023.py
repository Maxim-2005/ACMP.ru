N = int(input())
S = 0

for i in range(1, N+1):
    if N % i == 0:
        S += i
print(S)
