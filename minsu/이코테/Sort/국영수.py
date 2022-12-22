import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n) :
	li.append(sys.stdin.readline().split())
li.sort(key=lambda li : (-int(li[1]), int(li[2]), -int(li[3]), li[0]))
for i in li :
	print(i[0])