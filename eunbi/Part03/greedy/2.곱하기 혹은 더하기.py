datas = list(input())
datas.sort(reverse=True)

res = 0
for data in datas :
	if int(data) == 0 :
		res += 0
	elif int(data) != 0 and res != 0 :
		res *= int(data)
	else :
		res = int(data)

print(res)