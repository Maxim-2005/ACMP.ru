A, B = list(map(int, input().split()))
mode = str(input())
if A < B and mode == "heat":
	T = B
elif A > B and mode == "heat":
	T = A
elif A < B and mode == "auto":
	T = B
elif A > B and mode == "auto":
	T = B
elif A > B and mode == "freeze":
	T = B
elif A < B and mode == "freeze":
	T = A
elif mode == "fan":
	T = A
print(T)
