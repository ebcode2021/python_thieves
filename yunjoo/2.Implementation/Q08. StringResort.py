strList = list(input().rstrip())
strList.sort()
answer = 0
idx = 0
for chr in strList :
	if chr >= '0' and chr <= '9' :
		idx += 1
		answer += int(chr)
for i in range(idx, len(strList)) :
	print(strList[i], end = '')
print(answer)
