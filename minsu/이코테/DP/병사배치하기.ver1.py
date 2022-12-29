import sys
input = sys.stdin.readline
n = int(input())
dp = [1] * n
arr = list(map(int, input().split()))
arr.reverse()
for i in range(1, n) :
	for j in range(i) :
		if arr[i] > arr[j] :
			dp[i] = max(dp[i], dp[j] + 1) 
print(n - max(dp))