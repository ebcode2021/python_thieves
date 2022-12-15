def check(x, y) :
	if x >= 1 and x<= n and y >= 1 and y <= n :
		return 1
	return 0

# map_size && plans
n = int(input())
plans = input().split()

# start_location
x = 1
y = 1

# L, R, U, D
directions = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans :
	for i in range(4) :
		if (plan == directions[i] and check(x + dx[i], y + dy[i])) :
			x, y = x + dx[i], y + dy[i]

print(x, y)
