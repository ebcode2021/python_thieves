n, m = map(int, input().split())
li = sorted(list(map(int,input().split())))
sli = [0] * 10
for i in li :
	sli[i] += 1
i = 0
j = 0
ref = 0
while i < m :
	j += sli[li[i]]
	ref += sli[li[i]] * (len(li) - j)
	i += 1
print(ref)