x = input()
s = 0
temp = 0

for i in x:
	if i == "0":
		s += 1
		temp = max(temp, s)
	else:
		s = 0
print(temp)
