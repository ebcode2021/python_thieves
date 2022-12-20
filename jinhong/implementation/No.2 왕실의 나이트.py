answer = 0
position = input()
x = ord(position[0]) - 96
y = int(position[1])
offsets = [(-1, -2), (1, -2), (2, 1), (2, -1),\
		(1, 2), (-1, 2), (-2, 1), (-2, -1)]
for offset in offsets:
	if 1 <= x + offset[0] <= 8 and \
		1 <= y + offset[1] <= 8:
		answer += 1
print(answer)