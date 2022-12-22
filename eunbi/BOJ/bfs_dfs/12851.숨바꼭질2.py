import sys
from collections import deque

n, target = map(int, sys.stdin.readline().split())

visited = [False] * 100001
queue = deque([n])

if n == target :
	queue.popleft()
	print(0, 1, sep="\n")

find = 0
depth = 0
flag = 0
while queue :
	for j in range(len(queue)):
		v = queue.popleft()
		visited[v] = True
		for i in (v-1, v+1, v*2):
			if 0 <= i <= 100000 and not visited[i]:
				queue.append(i)
				if (i == target):
					find += 1
					flag = 1
	depth += 1
	if flag :
		break
	

if find  :
	print(depth)
	print(find)