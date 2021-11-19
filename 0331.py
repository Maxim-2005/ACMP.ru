a, b = map(int, input().split(":"))
t1, t2 = map(int, input().split())
print(str(((a + t1) + (b + t2) // 60) % 24).zfill(2) + ":" + str((b + t2) % 60).zfill(2))
