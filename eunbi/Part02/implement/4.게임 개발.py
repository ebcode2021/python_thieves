n , m = map(int, input().split())

# 현 x, 현 y, 현 방향
locate_x, locate_y, now_dir = map(int, input().split())
data = []
for _ in range(n) :
	data.append(list(map(int, input().split())))

#반시계 방향으로 체크
# 북 0 동 1 남 2 서 3
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
data[1][1] = 1

res = 1
now_dir = 0

total_check = 4
while total_check :
	if now_dir < 0 :
		now_dir = 3
	next_x = locate_x + directions[now_dir][0]
	next_y = locate_y + directions[now_dir][1]
	if data[next_x][next_y] == 0 :
		data[next_x][next_y] = 1
		locate_x = next_x
		locate_y = next_y
		res += 1
		total_check = 4
		continue
	now_dir -= 1
	total_check -= 1

print(res)
