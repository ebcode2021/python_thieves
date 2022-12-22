import sys
from collections import deque

def bfs(map, row, col):
	queue = deque()
	queue.append((row,col))
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]
	while queue:
		x, y = queue.popleft()
		map[x][y] = 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if not (0 <= nx < n) or not (0 <= ny < m):
				continue
			if map[nx][ny] == 0:
				queue.append((nx, ny))

answer = 0
n, m = map(int, sys.stdin.readline().split())
map = []
for _ in range(n):
	map.append([int(i) for i in sys.stdin.readline().rstrip()])
for row in range(n):
	for col in range(m):
		if map[row][col] == 0:
			answer += 1
			bfs(map, row, col)
print(answer)