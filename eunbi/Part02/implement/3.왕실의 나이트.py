# size : 8 * 8

n = input()

col, row = ord(n[0]) - ord('a') + 1, int(n[1])
directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cnt = 0
for direction in directions :
	tmp_col = col + direction[0]
	tmp_row = row + direction[1]
	if (tmp_col >= 1 and tmp_col <= 8 and tmp_row >=1 and tmp_row <= 8) :
		cnt += 1

print(cnt)