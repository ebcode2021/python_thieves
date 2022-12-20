N = int(input())
coins = [500, 100, 50, 10]
answer = 0
i = 0
while N:
	if coins[i] > N:
		i += 1
		continue
	N -= coins[i]
	answer += 1
print(answer)