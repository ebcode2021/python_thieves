N = int(input())
row, col = 1, 1
for command in input().split():
	if command == 'L':
		col = col - 1 if col > 1 else col
	elif command == 'R':
		col = col + 1 if col < N else col
	elif command == 'U':
		row = row - 1 if row > 1 else row
	elif command == 'D':
		row = row + 1 if row < N else row
print(row, col)