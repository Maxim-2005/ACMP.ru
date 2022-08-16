N, i, j = map(int, input().split())
print(min(N - abs(i - j) - 1, abs(i - j) - 1))
