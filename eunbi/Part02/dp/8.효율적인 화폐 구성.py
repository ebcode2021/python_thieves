import sys

f = sys.stdin.readline

n, m = map(int, f().split())
coin_lst = [int(f().rstrip()) for _ in range(n)]

d = [0] * 101
for coin in coin_lst :
	d[coin] = 1

def func(d, num) :
	if num > m :
		return
	for coin in coin_lst :
		if d[num + coin] == 0 :
			d[num + coin] = d[num] + 1
		else :
			d[num + coin] = min(d[num + coin], d[num] + 1)
		func(d, num + coin)

func(d, 0)
if d[m] == 0 :
	print(-1)
else :
	print(d[m])