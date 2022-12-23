import sys

f = sys.stdin.readline

cnt, length = map(int, f().split())
cakes = sorted(list(map(int, f().split)))

start = 0
end = cnt -1

res = 0
while (start <= end) :
	total = 0
	mid = (start + end) // 2
	for x in cakes :
		if x > mid : 
			total += x - mid
	if total < length :
		end = mid - 1
	else :
		result = mid
		start = mid + 1