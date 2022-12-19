n = int(input())

people = []
for _ in range(n) :
	people.append(list(map(int, input().split())))

res = []
for i in range(n) :
	j, cnt = 0, 0
	for j in range(n) :
		if j == i :
			continue
		if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
			cnt += 1
	res.append(str(cnt + 1))

print(' '.join(res))
