import sys
input = sys.stdin.readline
t = int(input())
for _ in range(0, t) :
	n, m = map(int, input().split())
	li = list(map(int, input().split()))
	_map = []
	for i in range(0, m) :
		tmp = []
		for j in range(0, n) :
			tmp.append(li[i + j * m])
		_map.append(tmp)
	for i in range(1, m) :
		for j in range(0, n) :
			if (j == 0) :
				_map[i][j] += max(_map[i - 1][j], _map[i - 1][j + 1])
			elif j == n - 1 :
				_map[i][j] += max(_map[i - 1][j], _map[i - 1][j - 1])
			else :
				_map[i][j] += max(_map[i - 1][j], _map[i - 1][j - 1], _map[i - 1][j + 1])
	print(max(_map[m - 1]))
			