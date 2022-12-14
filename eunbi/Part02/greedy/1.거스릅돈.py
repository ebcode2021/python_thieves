## solve_not using array
money = 1260
coin = 0

while money >= 500 :
	tmp = money // 500
	money -= 500 * tmp
	coin += tmp

while money >= 100 :
	tmp += money // 100
	money -= 100 * tmp
	coin += tmp

while money >= 50 :
	tmp += money // 50
	money -= 50 * tmp
	coin += tmp

while money >= 10 :
	tmp += money // 50
	money -= 50 * tmp
	coin += tmp

print("총 동전의 개수 : ", coin)

