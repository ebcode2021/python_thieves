import sys
from collections import deque

def bfs(map, queue, visited):
	while queue:
		current = queue.popleft()
		x, y, num = current
		if x == m-1 and y == n-1:
			print(num)
			break
		if 0 <= x+1 < m and map[y][x+1] == 1 and (x+1,y) not in visited:
			queue.append([x+1,y,num+1])
			visited.append((x+1,y))
		if 0 <= x-1 < m and map[y][x-1] == 1 and (x-1,y) not in visited:
			queue.append([x-1,y,num+1])
			visited.append((x-1,y))
		if 0 <= y+1 < n and map[y+1][x] == 1 and (x,y+1) not in visited:
			queue.append([x,y+1,num+1])
			visited.append((x,y+1))
		if 0 <= y-1 < n and map[y-1][x] == 1 and (x,y-1) not in visited:
			queue.append([x,y-1,num+1])
			visited.append((x,y-1))

n, m = map(int, sys.stdin.readline().split())
map = [[0 for _ in range(m)] for _ in range(n)]
for row in range(n):
	for i, num in enumerate(sys.stdin.readline().rstrip()):
		map[row][i] = int(num)
queue = deque()
queue.append([0,0,1])
visited = []
bfs(map, queue, visited)