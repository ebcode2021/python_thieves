import itertools

def solution(n, weak, dist):
	answer = 0
	weak = list(weak)
	weak_l = len(weak)
	combination = list(itertools.permutations(dist, len(dist)))
	for i in range(weak_l) :
		weak.append(weak[i] + n)
	print(combination)
	print(weak)
	return answer
solution(12, [1, 5, 6, 10], [1, 2, 3, 4])