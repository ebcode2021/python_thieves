def solution(food_times, K):
	index = 0
	time = 0
	food_len = len(food_times)
	if K >= sum(food_times):
		return -1
	while time < K:
		if food_times[index]:
			food_times[index] -= 1
		else:
			index += 1
			continue
		time += 1
		index += 1
		if index == food_len:
			index = 0
	while food_times[index] == 0:
		index += 1
		if index == food_len:
			index = 0
	return index + 1

food_times = [3, 1, 2]
K = 5
print(solution(food_times, K), 1)

food_times = [3, 1, 2]
K = 4
print(solution(food_times, K), 3)

food_times = [3, 1, 2]
K = 6
print(solution(food_times, K), -1)
