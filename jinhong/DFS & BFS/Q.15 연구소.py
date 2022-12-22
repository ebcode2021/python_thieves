import sys
from collections import deque
from copy import deepcopy

def bfs(map, row, col):
	queue = deque()
	queue.append((col, row))
	dx = [1, 0, -1 ,0]
	dy = [0, -1, 0, 1]
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if not (0 <= nx < m and 0 <= ny < n):
				continue
			if map[ny][nx] == 0:
				map[ny][nx] = 2
				queue.append((nx,ny))

def spread_virus(map):
	for row in range(n):
		for col in range(m):
			if map[row][col] == 2:
				bfs(map, row, col)
	safe_zone = 0
	for row in range(n):
		for col in range(m):
			if map[row][col] == 0:
				safe_zone += 1
	return safe_zone

answer = []
n, m = map(int, sys.stdin.readline().split())
map = []
for _ in range(n):
	map.append([int(i) for i in sys.stdin.readline().split()])
for i in range((n*m)-2):
	for j in range(i+1, (n*m)-1):
		for k in range(j+1, n * m):
			i_x, i_y = i%m, i//m
			j_x, j_y = j%m, j//m
			k_x, k_y = k%m, k//m
			if map[i_y][i_x] or map[j_y][j_x] or map[k_y][k_x]:
				continue
			copy = deepcopy(map)
			copy[i_y][i_x] = 1
			copy[j_y][j_x] = 1
			copy[k_y][k_x] = 1
			answer.append(spread_virus(copy))
print(max(answer))

""" 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0 
"""