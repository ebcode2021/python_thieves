li = list(map(int,input()))
cnt = 0
ref = 0
for i in li :
	if i == 0 : cnt += 1
	ref += i
if (cnt == 0 or ref % 3 != 0) :
	print("-1")
	exit()
li.sort(reverse=True)
print(''.join(map(str, li)))