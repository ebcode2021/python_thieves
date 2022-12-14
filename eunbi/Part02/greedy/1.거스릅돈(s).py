## solve_using array

money = 1260
coin = 0
coin_unit = [500, 100, 50, 10]

for unit in coin_unit :
	coin += money // unit
	money %= unit

print("총 동전의 개수 : ", coin)

