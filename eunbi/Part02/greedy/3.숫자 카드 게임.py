rows, cols = map(int, input().split())

res = 0

for _ in range(rows) :
	tmp_list = list(map(int, input().split()))
	res = max(res, min(tmp_list))

print(res)
