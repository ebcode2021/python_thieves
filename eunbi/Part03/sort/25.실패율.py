# 다시 풀기

def solution(N, stages) :
	stage_len = len(stages)

	res = []
	divided = stage_len
	for i in range(1, N + 1) :
		cnt = 0
		for j in range(stage_len) :
			if stages[j] == i :
				cnt += 1
		if cnt == 0 :
			res.append((i,0))
		else :
			res.append((i, cnt / divided))
			divided -= cnt

	res.sort(reverse=True, key=lambda x : (x[1], -x[0]))
	answer = []
	for i in range(len(res)) :
		answer.append(res[i][0])
	return answer
