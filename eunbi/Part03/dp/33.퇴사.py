import sys

f = sys.stdin.readline

num = int(f())

schedule = []
for _ in range(num) :
	schedule.append(list(map(int, f().split())))

d = [0] * 16
idx = 0

