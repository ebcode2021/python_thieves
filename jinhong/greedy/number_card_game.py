row, col = map(int, input().split())
mins = []
for cards in range(row):
	mins.append(min(list(map(int, input().split()))))
print(max(mins))