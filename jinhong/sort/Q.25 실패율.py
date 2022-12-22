def solution(N, stages):
	stages.sort()
	failure_rate = []
	failed = 0
	number_of_players = len(stages)
	passed = number_of_players
	i = 0
	for stage in range(1,N+1):
		while i < number_of_players and stages[i] <= stage:
			failed += 1
			i += 1
		failure_rate.append((stage, failed/passed))
		passed -= failed
		failed = 0
	failure_rate.sort(key=lambda x:(-x[1], x[0]))
	print([fail[0] for fail in failure_rate])

N = 5
stages = [2,1,2,6,2,4,3,3]
solution(N, stages)

N = 4
stages = [4,4,4,4,4]
solution(N, stages)