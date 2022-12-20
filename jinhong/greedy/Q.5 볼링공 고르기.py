answer = 0
N, M = map(int, input().split())
balls = [int(ball) for ball in input().split()]
for i in range(N):
	for j in range(i+1, N):
		if balls[i] != balls[j]:
			answer += 1
print(answer)