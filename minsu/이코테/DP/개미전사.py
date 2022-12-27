import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(2, n) :
	arr[i] = max(arr[i] + arr[i - 2], arr[i - 1])
print(arr[n - 1])