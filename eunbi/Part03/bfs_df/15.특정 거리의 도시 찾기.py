from collections import deque
import sys

f = sys.stdin.readline
total_city, total_road, distance, start = map(int, f().split())
graph = [[] for i in range(total_city + 1)]

for _ in range(total_road) :
	i, j = map(int, f().split())
	graph[i].append(j)

visited = [-1] * (total_city + 1)
visited[start] = 0

queue = deque([start])
while queue :
	now = queue.popleft()
	for i in graph[now] :
		if visited[i] == -1 :
			visited[i] = visited[now] + 1
			queue.append(i)

result = []
for i in range(1, total_city + 1) :
	if visited[i] == distance :
		result.append(i)

result.sort()
if result :
	print("\n".join(str(res) for res in result))
else :
	print(-1)
