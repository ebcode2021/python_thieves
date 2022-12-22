import sys

f = sys.stdin.readline

n = int(f())
lst = []
for _ in range(n) :
	name, score = f().split()
	lst.append([name, int(score)])

lst.sort(reverse=True, key=lambda x : x[1])

for i in lst :
	print(i[0], end=' ')