from collections import deque

def bfs(graph, start, visited) :
	queue = deque([start])
	graph[start] = True
	while queue :
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v] :
			if not visited[i] :
				queue.append(i)
				visited[i] = True

# 2차원 리스트로 표현
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)