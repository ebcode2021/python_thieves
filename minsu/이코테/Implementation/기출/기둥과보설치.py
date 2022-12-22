def isbuild(answer) :
	for i in answer :
		x, y, kinds = i
		if kinds == 0 :
			if y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer :
				continue
			else :
				return False
		if kinds == 1 :
			if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer) :
				continue
			else :
				return False
	return True
		

def solution(n, build_frame):
	answer = []
	
	for i in build_frame :
		if i[3] == 1 :
			answer.append([i[0], i[1], i[2]])
			if not isbuild(answer) :
				answer.remove([i[0], i[1], i[2]])
		if i[3] == 0 :
			answer.remove([i[0], i[1], i[2]])
			if not isbuild(answer) :
				answer.append([i[0], i[1], i[2]])
	answer.sort()
	return answer
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))