n, m = map(int, input().split())
name = ''
t = m * 1000 + 1

for i in range(n):
	nameT = input()
	S = sum(map(int, input().split()))
	if t > S:
		name = nameT
		t = S
print(name)
