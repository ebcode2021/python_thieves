import heapq
def solution(food_times, k):
	h = []
	for i in range(len(food_times)) :
		heapq.heappush(h, (food_times[i], i))
	len_ = len(food_times)
	temp = 0
	while len_ :
		eat = (h[0][0] - temp) * len_
		temp = h[0][0]
		if (k >= eat) :
			k -= eat
			len_ -= 1
			heapq.heappop(h)
		else :
			h.sort(key = lambda x: x[1])
			return (h[k % len_][1] + 1)
	return -1
print(solution([1, 3, 5, 3, 2], 10))