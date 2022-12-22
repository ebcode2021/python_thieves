import sys
import heapq
from collections import deque

udlr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, k = map(int, sys.stdin.readline().split())
map_ = []
for _ in range(n) :
	map_.append(list(map(int, sys.stdin.readline().split())))
s, e_x, e_y = map(int, input().split())
queue = []
for i in range(n) :
	for j in range(n) :
		if (map_[i][j] != 0) :
			heapq.heappush(queue, [map_[i][j], i, j])
queue1 = deque()
for _ in range(len(queue)) :
	queue1.appendleft(list(heapq.heappop(queue)))
for _ in range(s) :
	for k in range(len(queue1)) :
		value, y, x = list(queue1.pop())
		for xy in udlr :
			n_x = x + xy[0]
			n_y = y + xy[1]
			if (0 <= n_y < n and 0 <= n_x < n) :
				if map_[n_y][n_x] == 0 :
					queue1.appendleft([value, n_y, n_x])
					map_[n_y][n_x] = value
print(map_[e_x - 1][e_y - 1])

