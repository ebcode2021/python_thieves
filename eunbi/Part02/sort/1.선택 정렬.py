array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
	min_idx = i
	for j in range(i, len(array)) :
		if array[j] < array[min_idx] :
			min_idx = j
	array[i], array[min_idx] = array[min_idx], array[i]

print(array)