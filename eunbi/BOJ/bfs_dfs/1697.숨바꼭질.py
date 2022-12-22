from collections import deque

n, k = map(int, input().split())
queue = deque([n])

visited = [0] * 1000001
visited[n] = 1

while queue :
	v = queue.popleft()
	if v-1 >= 0 and not visited[v - 1]:
		queue.append(v - 1)
		visited[v - 1] = visited[v] + 1
	if  v+1 <= 1000000 and not visited[v+1]:
		queue.append(v + 1)
		visited[v+1] = visited[v] + 1
	if  v * 2 <= 1000000 and not visited[v * 2] :
		queue.append(v * 2)
		visited[v * 2] = visited[v] + 1
	if v == k :
		print(visited[v] - 1)
		break



