import queue
import sys
n, m = map(int, input().split())
arr = []
for _ in range(n) :
	arr.append(list(input()))
udlr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ref = 0
for i in range(0, n) :
	for j in range(0, m) :
		if arr[i][j] == '0' :
			ref += 1
			queue1 = queue.Queue()
			queue1.put([i, j])
			while int(queue1.qsize()) :
				for _ in range(int(queue1.qsize())) :
					x, y = list(queue1.get())
					for k in udlr :
						n_x = x + k[0]
						n_y = y + k[1]
						if n_x >= 0 and n_x < n and n_y >= 0 and n_y < m :
							if arr[n_x][n_y] == '0' :
								queue1.put([n_x, n_y])
								arr[n_x][n_y] = '1'
print(ref)

