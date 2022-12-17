# 다시풀기

num = int(input())
datas= list(map(int, input().split()))

datas.sort()

res = 1
for data in datas :
	if res < data:
		break
	res += data

print(res)