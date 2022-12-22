from collections import deque
n, m = map(int, input().split())
map1 = []
for _ in range(n) :
	map1.append(list(input()))
visit = [[0] * m for _ in range(n)]
udlr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt = 1
queue1 = deque()
queue1.appendleft([0, 0])
visit[0][0] = 1
while len(queue1) :
	for _ in range(len(queue1)) :
		x, y = list(queue1.pop())
		for next in udlr :
			n_x = x + next[0]
			n_y = y + next[1]
			if (n_x >= 0 and n_x < n and n_y >= 0 and n_y < m) :
				if (map1[n_x][n_y] == '1' and visit[n_x][n_y] == 0) :
					visit[n_x][n_y] = visit[x][y] + 1
					queue1.appendleft([n_x, n_y])
	cnt += 1
print(visit[n - 1][m - 1])