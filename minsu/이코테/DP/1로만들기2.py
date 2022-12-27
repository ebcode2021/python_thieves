import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
visit = [0] * (n + 1)
visit[n] = -1
queue.appendleft(n)
while len(queue) :
	now = queue.pop()
	if (now == 1) :
		break
	if now - 1 > 0 and visit[now - 1] == 0 :
		queue.appendleft(now - 1)
		visit[now - 1] = now
	if now % 3 == 0 and visit[now // 3] == 0 :
		queue.appendleft(now // 3)
		visit[now // 3] = now
	if now % 2 == 0 and visit[now // 2] == 0 :
		queue.appendleft(now // 2)
		visit[now // 2] = now
i = 1
cnt = 0
li = []
while visit[i] != -1 :
	li.append(i)
	cnt += 1
	i = visit[i]
print(cnt)
print(n, end=" ")
for i in reversed(li) :
	print(i, end=" ")
	

			

	
