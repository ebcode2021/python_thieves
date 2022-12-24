import sys

f = sys.stdin.readline

n = int(f())
datas = list(map(int, f().split()))

def binary_search(datas, start, end) :
	while start <= end :
		mid = (start + end) // 2
		if datas[mid] == mid :
			return datas[mid]
		elif datas[mid] > mid :
			end = mid - 1
		else :
			start = mid + 1
	return None

res = binary_search(datas, 0, len(datas) - 1)

if res != None :
	print(res)
else :
	print(-1)