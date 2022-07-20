x1, y1, x2, y2, x3, y3 = map(int, input().split())
a = ((abs(y1 - y2) ** 2) + (abs(x1 - x2) ** 2)) ** 0.5
b = ((abs(y2 - y3) ** 2) + (abs(x2 - x3) ** 2)) ** 0.5
c = ((abs(y3 - y1) ** 2) + (abs(x3 - x1) ** 2)) ** 0.5
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(round(S * 10) / 10)
