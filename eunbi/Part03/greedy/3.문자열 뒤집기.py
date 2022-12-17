data = list(map(int, input()))

inform = [0, 0]

tmp = data[0]
inform[data[0]] = 1
for i in data :
	if tmp != i:
		tmp = i
		inform[i] += 1
print(min(inform))