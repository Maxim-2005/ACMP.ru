N = int(input())
arr5 = list(map(int, input().split()))
arr3 = arr5.copy()
arr3.reverse()
arr1= arr5.copy()
arr1.sort()

summ = [0, 0, 0]

for i in range(N):
    summ[0] += arr1[i]
    summ[1] += arr3[i]
    summ[2] += arr5[i]

print(min(summ))
