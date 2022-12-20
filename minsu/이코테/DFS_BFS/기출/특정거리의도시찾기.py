import sys
from collections import defaultdict, deque
n, m, k, x = map(int, input().split())
dict1 = defaultdict(list)
for _ in range(m) :
	s, e = map(int, sys.stdin.readline().split())
	dict1[s].append(e)
visit = [0] * (n + 1)
deque1 = deque()
visit[x] = 1
deque1.appendleft(x)
while len(deque1) :
	now_node = deque1.pop()
	for i in dict1[now_node] :
		if (visit[i] == 0) :
			visit[i] = visit[now_node] + 1
			deque1.appendleft(i)
find = False
for i in range(1, n + 1) :
	if visit[i] - 1 == k :
		print(i)
		find = True
if (not find) :
	print(-1)
		

