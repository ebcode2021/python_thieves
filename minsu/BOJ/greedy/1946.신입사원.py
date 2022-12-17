n = int(input())
for _ in range(n) :
	repeat = int(input())
	li = []
	cnt = 0
	for _ in range(repeat) :
		value = list(map(int, input().split()))
		li.append(value)
	li.sort(key=lambda x:x[0])
	ac = 10000000
	for i in li :
		if i[1] < ac :
			ac = i[1]
			cnt += 1
	print(cnt)