# 다시 풀기

n = int(input())
data = list(map, input().split())
data.sort()

target = 1
for x in data :
	if target < x :
		break
	target += x
print(target)