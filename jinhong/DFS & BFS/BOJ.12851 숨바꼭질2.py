from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append((N,0))
min_move = abs(N-K)
visited = [0 for _ in range(100001)]
while queue:
	cur, move = queue.popleft()
	if move > min_move:
		continue
	visited[cur] += 1
	if cur == K:
		min_move = move
		continue
	if 0 <= cur -1 <= 100000 and not visited[cur-1]:
		queue.append((cur-1, move+1))
	if 0 <= cur + 1 <= 100000 and not visited[cur+1]:
		queue.append((cur+1, move+1))
	if 0 <= 2*cur <= 100000 and not visited[2*cur]:
		queue.append((2*cur, move+1))
print(min_move)
print(visited[K])