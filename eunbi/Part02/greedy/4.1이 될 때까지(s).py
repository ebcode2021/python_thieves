# solve_1 : 시간 복잡도를 덜 고려한 경우
n, k = map(int, input().split())
result = 0

# n이 k 이상이라면 k로 계속 나누기
while n >= k :
	# n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
	while n % k != 0 :
		n -= 1
		result += 1
	n //= k
	result += 1

while n > 1 :
	n -= 1
	result += 1

print(result)

# solve_2 : 시간 복잡도를 좀 더 고려한 경우
n, k = map(int, input().split())
result = 0

while 1 :
	# (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
	target = (n // k) * k
	result += (n - target)
	n = target
	# N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
	if n < k :
		break
	# K로 나누기
	result += 1
	n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
