from collections import deque

col, row = map(int, input().split())
frames = []
for i in range(col) :
	frames.append(list(map(int, input())))

# 이동할 방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
	queue = deque()
	queue.append((x, y))
	while queue :
		x, y = queue.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= col or ny >= row :
				continue
			if frames[nx][ny] == 1 :
				frames[nx][ny] = frames[x][y] + 1
				queue.append((nx, ny))
	return frames[col - 1][row - 1]

print(bfs(0, 0))
