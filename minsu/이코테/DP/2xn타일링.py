import sys

n = int(sys.stdin.readline())
arr = [0] * n
if (n == 1) :
	print(1)
	exit()
arr[0] = 1
arr[1] = 2
for i in range(2, n) :
	arr[i] = (arr[i - 1] + arr[i - 2]) % 10007
print(arr[n - 1])