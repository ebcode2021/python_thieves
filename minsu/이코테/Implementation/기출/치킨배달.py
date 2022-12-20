import sys

n, m = list(map(int, sys.stdin.readline().split()))
save = []
min_ = 1000000000000

def yami(chicken, house, depth, idx) :
	i = idx
	global min_
	global save
	global m
	
	while i < len(chicken) :
		save.append(chicken[i])
		if (depth < m - 1) :
			yami(chicken, house, depth + 1, i + 1)
		else :
			cost = 0
			for j in house :
				n_cost = 100000000000
				for k in save : 
					n_cost = min(n_cost, abs(j[0] - k[0]) + abs(j[1] - k[1]))
				cost += n_cost
			min_ = min(cost, min_)
		save.remove(chicken[i])
		i += 1

		
	
house = []
chicken = []
for i in range(0, n) :
	arr = list(map(int, sys.stdin.readline().split()))
	for j in range(0, n) :
		if arr[j] == 1 : house.append([i + 1, j + 1])
		elif arr[j] == 2 : chicken.append([i + 1, j + 1])

yami(chicken, house, 0, int(0))
print(min_)
