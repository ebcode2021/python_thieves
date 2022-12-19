from collections import deque

pointList = list(input().rstrip())
pointList[0] = ord(pointList[0]) - 96
pointList[1] = int(pointList[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

dq = deque() 
x, y = pointList
cur_x, cur_y = 0, 0
dq.append((x, y))
cnt = 0
if dq :
	x, y = dq.popleft()
	for i in range(8) :
		cur_x = dx[i] + x
		cur_y = dy[i] + y
		if cur_x < 1 or cur_y < 1 or cur_x > 8 or cur_y > 8 :
			continue
		else : 
			dq.append((cur_x, cur_y))
			cnt += 1
print(cnt)