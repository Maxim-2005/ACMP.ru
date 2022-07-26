n = int(input());
arr = []
if n - 8 > 0 :
	arr.append(n - 8)
if (n - 1) % 8 > 0:
	arr.append(n - 1)
if n % 8 != 0:
	arr.append(n + 1)
if n < 57:
	arr.append(n + 8)
print(*arr);
