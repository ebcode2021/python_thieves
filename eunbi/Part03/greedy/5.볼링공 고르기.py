import itertools

num, max = map(int, input().split())
balls = list(map(int, input().split()))
datas = itertools.combinations(balls, 2)

cnt = 0
for data in datas :
	if data[0] == data[1] :
		continue
	cnt += 1

print(cnt)