k1, l1, m1 = map(int, input().split());
k2, l2, m2 = map(int, input().split());
k = min((k1 - (k1 * l1) // 100), (k2 - (k2 * l2) // 100))
print((k1 - k) * m1 + (k2 - k) * m2)
