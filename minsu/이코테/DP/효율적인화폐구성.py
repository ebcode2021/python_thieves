import sys

input = sys.stdin.readline
n, m = map(int, input().split())
coin = []
for _ in range(0, n) :
	coin.append(int(input()))
arr = [10001] * (m + 1)
arr[0] = 0
for i in coin :
	for j in range(i, m + 1) :
		if arr[j - i] != 10001 :
			arr[j] = min(arr[j], arr[j - i] + 1)
if arr[m] == 10001 :
	print(-1)
else :
	print(arr[m])
