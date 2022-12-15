N, K = map(int, input().split())
answer = 0
while True:
	if N == 1:
		break
	if N % K == 0:
		N //= K
	else:
		N -= 1
	answer += 1
print(answer)