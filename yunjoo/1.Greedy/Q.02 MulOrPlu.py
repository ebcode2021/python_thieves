numList = list(map(int, input().rstrip()))
i = 0
answer = 0
num_len = len(numList)

for idx in range(num_len) :
	if numList[idx] == 0 or numList[idx] == 1 or answer == 0 or answer == 1 :
		answer += numList[idx]
	else: 
		answer *= numList[idx]
print(answer)