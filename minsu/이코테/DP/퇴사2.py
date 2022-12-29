import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [0] * (n + 2)
for _ in range(n) :
	arr.append(list(map(int, input().split())))
for i in range(0, n) :
	days, cost = arr[i]
	if (i + days <= n) :
		dp[days + i] = max(dp[i] + cost, dp[days + i])
	dp[i + 1] = max(dp[i + 1], dp[i])
print(dp[n])