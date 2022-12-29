import sys

def bs(dp, s, e, ele) :
	while s < e :
		mid = (s + e) // 2
		if ele > dp[mid] :
			s = mid + 1
		else :
			e = mid
	return e


input = sys.stdin.readline
n = int(input())
dp = []
arr = list(map(int, input().split()))
arr.reverse()
dp.append(arr[0])
size = 0
for i in range(1, n) :
	if arr[i] > dp[size] :
		dp.append(arr[i])
		size += 1
	pos = bs(dp, 0, size, arr[i])
	dp[pos] = arr[i]
print(n - (size + 1))