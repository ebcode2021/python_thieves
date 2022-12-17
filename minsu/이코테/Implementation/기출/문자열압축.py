def solution(s) :
	s_len = len(s)
	roop = s_len // 2
	min_ = len(s)
	for i in range(1, roop + 1) :
		str_ = s[0:i]
		j = i
		cnt = 1
		ref = 0
		while True :
			end = j + i
			if (s_len < end) :
				end = s_len 
			compare_str_ = s[j:end]
			if str_ == compare_str_ :
				cnt += 1
			else :
				if (cnt > 1) :
					ref += len(str(cnt))
				ref += len(str_)
				str_ = compare_str_
				cnt = 1
			if (s_len == end) :
				if (cnt > 1) :
					ref += len(str(cnt))
				ref += len(compare_str_)
				break
			j += i
		if min_ > ref :
			min_ = ref
	return (min_)
print(solution("aaaaaaaaaa"))

				

		
