n = int(input())
li = []
for _ in range(n) :
	x, y = list(input().split())
	li.append([x, int(y)])
li.sort(key=lambda li:li[1])
for x in li :
	print(x[0], end=' ')