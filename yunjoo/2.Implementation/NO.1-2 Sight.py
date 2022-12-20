#다시 풀기!
N = int(input())
cnt = 0
for hours in range(N + 1) :
	for minutes in range(60) : 
		for seconds in range(60) :
			if '3' in str(hours) + str(minutes) + str(seconds) :
				cnt += 1
print(cnt)