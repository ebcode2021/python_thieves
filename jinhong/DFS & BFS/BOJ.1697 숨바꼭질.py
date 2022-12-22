from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append(N)
visited = [0 for _ in range(100001)]
while queue:
	cur = queue.popleft()
	if cur == K:
		print(visited[cur])
		break
	if 0 <= cur -1 <= 100000 and not visited[cur-1]:
		queue.append(cur-1)
		visited[cur-1] = visited[cur] + 1
	if 0 <= cur + 1 <= 100000 and not visited[cur+1]:
		queue.append(cur+1)
		visited[cur+1] = visited[cur] + 1
	if 0 <= 2*cur <= 100000 and not visited[2*cur]:
		queue.append(2*cur)
		visited[2*cur] = visited[cur] + 1