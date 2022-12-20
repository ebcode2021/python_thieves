strList = list(map(int, input().rstrip()))
div_idx = len(strList) // 2
sumValue = 0
for i in range(div_idx) :
	sumValue += strList[i]
for j in range(div_idx, len(strList)) :
	sumValue -= strList[j]
if sumValue == 0 : 
	print("LUCKY")
else :
	print("READY")