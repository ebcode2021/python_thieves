import sys
from collections import deque

def bfs(map):
	queue = deque()
	queue.append((0,0))
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]
	while queue:
		x, y = queue.popleft()
		if x == m-1 and y == n-1:
			return map[y][x]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if not (0 <= nx < m and 0 <= ny < n):
				continue
			if map[ny][nx] == 0:
				continue
			map[ny][nx] = map[y][x] + 1
			queue.append((nx, ny))

answer = 0
n, m = map(int, sys.stdin.readline().split())
map = []
for _ in range(n):
	map.append([int(i) for i in sys.stdin.readline().rstrip()])
print(bfs(map))
