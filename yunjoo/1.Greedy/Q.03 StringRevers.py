numList = list(map(int, input().rstrip()))
checkList = [0, 0]
num_len = len(numList) - 1
for idx in range(num_len):
	if idx == 0 : 
		if numList[0] == 1 :
			checkList[1] += 1
		else : 
			checkList[0] += 1
	if numList[idx] != numList[idx + 1] :
		checkList[numList[idx + 1]] += 1
if checkList[0] == 1 or checkList[1] == 1 :
	print(1)
elif checkList[0] > checkList[1] : 
	print(checkList[1])
else : 
	print(checkList[0])