x1, y1, x2, y2 = map(int, input().split())
xA, yA  = map(int, input().split())
xB = yB = 0

if x1 == x2:
	xB, yB = x1 - (xA- x1), yA
else:
	xB, yB = xA, y1 - (yA- y1)

print(xB, yB)
