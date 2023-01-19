s = input()
t = 0
arr = "abcdefghijklmnopqrstuvwxyz"
arr1= []

for i in s:
	t += 1
	if i == "1":
		arr1.append(arr[t-1])
		t = 0
print(''.join(arr1))

