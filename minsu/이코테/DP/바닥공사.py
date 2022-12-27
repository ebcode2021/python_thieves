import sys
n = int(sys.stdin.readline())
arr = [0] * n
arr[0] = 1
arr[1] = 3
for i in range(2, n) :
	arr[i] = (arr[i - 1] + (arr[i - 2] * 2)) % 796796
print(arr[n - 1])