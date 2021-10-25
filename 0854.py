A, B = map(int, input().split())
mode = input()

if mode == "freeze":
        print(min(A, B))
elif mode == "heat":
        print(max(A, B))
elif mode == "auto":
        print(B)
else:
        print(A)
