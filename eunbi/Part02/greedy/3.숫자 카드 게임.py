rows, cols = map(int, input().split())

max = 0

for _ in range(rows) :
	tmp_list = list(map(int, input().split()))
	if (max < min(tmp_list)) :
		max = min(tmp_list)

print(max)
