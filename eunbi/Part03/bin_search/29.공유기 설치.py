import sys

f = sys.stdin.readline

homes, shares = map(int, f().split())
datas = []
for _ in range (homes) :
	datas.append(int(f().rstrip()))
datas.sort()

candidates = [0, len(datas) - 1]
def binary_search(datas, shares, start, end) :
	mid = (start + end) // 2
	if start > end or not (0 < mid < len(datas) - 1):
		return
	candidates.append(mid)
	if shares == 0 :
		return
	binary_search(datas, shares - 1, start, mid - 1)
	binary_search(datas, shares - 1, mid + 1, end)

binary_search(datas, shares - 2, 0, len(datas) - 1)

res = 1e9
print(candidates)
for candidate in candidates :
	if candidate == 0 :
		distance = datas[candidate + 1] - datas[candidate]
	elif candidate == len(datas) - 1:
		distance = datas[candidate] - datas[candidate - 1]
	else :
		distance = max(datas[candidate] - datas[candidate - 1], datas[candidate + 1] - datas[candidate])
	res = min(distance, res)
print(res)