# 인접 리스트(Adjacency List)
# 모든 노드에 연결된 노드에 대한 정보를 차례로 연결하여 저장

graph = [[] for _ in range(3)]

# 노드 0
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1
graph[1].append((0, 7))

# 노드 2
graph[2].append((0, 5))

print(graph)