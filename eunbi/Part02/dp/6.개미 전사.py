import sys

f = sys.stdin.readline

num = int(f())
storage = list(map(int, f().split()))

d = [0] * (num + 1)
d[0] = storage[0]
d[1] = storage[1]
d[2] = storage[2] + d[0]

for i in range(3, num) :
	d[i] = max(d[i - 2], d[i - 3]) + storage[i]

print(max(d))