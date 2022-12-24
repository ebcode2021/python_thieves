# O(logN)
# 1) 이진트리

import sys

f = sys.stdin.readline

N, m = map(int, f().split())
datas = sorted(list(map(int, f().split())))


def binary_search(datas, target, start, end) :
	while start <= end :
		mid = (start + end) // 2
		if datas[mid] >= target :
			end = mid - 1
		elif datas[mid] == target :
			return mid
		else :
			start = mid + 1
	return mid

location = binary_search(datas, m, 0, len(datas) - 1)

res = 0

for i in range(location, len(datas)) :
	if datas[i] != m :
		break
	res += 1
if res == 0 :
	print(-1)
else :
	print(res)


