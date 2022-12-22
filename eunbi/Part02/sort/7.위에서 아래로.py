import sys

f = sys.stdin.readline

n = int(f())
lst = []
for _ in range(n) :
	lst.append(f().strip())

lst.sort(reverse=True)

print(' '.join(lst))