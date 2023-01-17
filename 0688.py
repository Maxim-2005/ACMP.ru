x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
N = int(input())
res = "NO"

for i in range(N):
	x, y = map(int, input().split())
	sus = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
	sab = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
	if sus <= sab / 2:
		res = i + 1
		break
print(res)
