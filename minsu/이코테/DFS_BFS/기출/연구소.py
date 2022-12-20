import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
max_ = 0
udlr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def find_area(map_) :
	global max_
	deque1 = deque()
	for i in range(n) :
		for j in range(m) :
			if (map_[i][j] == 2) :
				deque1.appendleft([i, j])
				while len(deque1) :
					y, x = list(deque1.pop())
					for z in udlr :
						n_y = y + z[0]
						n_x = x + z[1]
						if n_y >= 0 and n_y < n and n_x >= 0 and n_x < m :
							if (map_[n_y][n_x] == 0) :
								map_[n_y][n_x] = 3
								deque1.appendleft([n_y, n_x])

	cnt = 0
	for i in map_ :
		for j in i :
			if j == 0 :
				cnt += 1
	max_ = max(max_, cnt)

def walling(map_, x, y, depth) :
	global n
	global m
	i = x
	j = y
	for i in range(x, n) :
		for j in range(0, m) :
			if map_[i][j] == 0 :
				map_[i][j] = 1
				if (depth < 2) :
					walling(map_, i, j + 1, depth + 1)
				else :
					find_area(copy.deepcopy(map_))
				map_[i][j] = 0
			
map_ = []
for _ in range(n) :
	map_.append(list(map(int, input().split())))
walling(map_, 0, 0, 0)
print(max_)