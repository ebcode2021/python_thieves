# 인접 행렬(Adjacency Matirx)
# 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식

# 연결 되어 있지 않은 노드 : 무한(INF)

INF = 999999999

graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]
print(graph)