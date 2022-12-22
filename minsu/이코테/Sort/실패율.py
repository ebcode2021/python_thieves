def solution(N, stages):
	cnt = [0] * (N + 2)
	for i in stages :
		cnt[i] += 1
	answer = []
	tmp = 0
	len_ = len(stages)
	for i in range(1, N + 1) :
		if (len_ - tmp == 0) :
			answer.append([0, i])
		else :
			answer.append([cnt[i] / (len_ - tmp), i]) 
		tmp += cnt[i]
	answer.sort(key=lambda answer: (-answer[0], answer[1]))
	answer1 = []
	for i in answer :
		answer1.append(i[1])
	return answer1
print(solution(4, [1, 1, 1, 1]))