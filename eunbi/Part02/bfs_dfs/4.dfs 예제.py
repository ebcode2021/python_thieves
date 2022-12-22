# DFS 메서드 정의
def dfs(graph, start, visited) :
	visited[start] = True
	print(start, end=' ')
	for i in graph[start] :
		if not visited[i] :
			dfs(graph, i, visited)

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

visited = [False] * 8

dfs(graph, 1, visited)