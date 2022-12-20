# 다시 풀기!

from collections import deque

N, M = map(int, input().split())
player = list(map(int, input().split()))
mapList = []
for i in range(N) :
	mapList.append(list(map(int, input().split())))
play_x = player[0]
play_y = player[1]
play_d = player[2]
mapList[play_y][play_x] = play_d
dc = [0, 1, 2, 3]
dd = [3, 0, 1, 2]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dq = deque()
dq.append((play_x, play_y, play_d))
cnt = 1
while dq :
	x, y, d = dq.popleft()
	for i in range(4) :
		print("d: ", end = ' ')
		print(d)
		if play_d != dc[i] :
			print("hello!")
			print("ii : ", end = ' ')
			print(i)
			continue
		else :
			play_d = dd[i]
			print(play_d)
			print("i : ", end = ' ')
			print(i)
			if x + dx[i] >= 0 and x + dx[i] < M and y + dy[i] >= 0 and y + dy[i] < N :
				print("test : ", end = ' ')
				print(x + dx[i], y + dy[i])
				if mapList[y + dy[i]][x + dx[i]] == 0 :
					print("mapList!! : ", end = ' ')
					print(mapList[y + dy[i]][x + dx[i]])
					mapList[y][x] = 5
					cnt += 1
					play_x = x + dx[i]
					play_y = y + dy[i]
					dq.append((play_x, play_y, play_d))
				else :
					print("else!! : ", end = ' ')
					print(play_x, play_y, play_d)
					continue
print(cnt)









