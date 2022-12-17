def is_possible_price(price, coins):
	total = 0
	for i in range(len(coins)):
		next_total = total + coins[0]
		if total + coins[i] <= price:
			total += coins[i]
		elif total + coins[i] > price:
			break
		if total == price:
			return True
	return False

n = int(input())
coins = sorted([int(i) for i in input().split()], reverse=True)
answer = 1
while True:
	if not is_possible_price(answer, coins):
		break
	answer += 1
print(answer)