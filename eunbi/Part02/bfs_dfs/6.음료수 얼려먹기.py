# n : 세로 길이 | m : 가로 길이
n, m = map(int, input().split())
frame = []

for i in range(n) :
	frame.append(list(map(int,input())))

def dfs(col, row) :
	if col <= -1 or col >= n or row <= -1 or row >= m :
		return False
	# 현재 노드를 아직 미방문
	if frame[col][row] == 0 :
		frame[col][row] = 1
		# 상, 하, 좌, 우
		dfs(col - 1, row)
		dfs(col + 1, row)
		dfs(col, row - 1)
		dfs(col, row + 1)
		return True
	return False

res = 0
for col in range(n) :
	for row in range(m) :
		if dfs(col, row) == True :
			res += 1

print(res)