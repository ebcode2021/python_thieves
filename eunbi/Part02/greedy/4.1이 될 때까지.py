n, m = map(int, input().split())
cnt = 1
res = m

while (n >= res * m) :
	res *= m
	cnt += 1

while (n != res) :
	res, cnt = res + 1, cnt + 1

print(cnt)