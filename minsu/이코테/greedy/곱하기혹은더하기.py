li = list(map(int,input()))
ref = li[0]
for i in range(1, len(li)) :
	ref = ref * li[i] if ref * li[i] > ref + li[i] else ref + li[i]
print(ref)