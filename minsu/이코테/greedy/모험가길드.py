n = int(input())
li = list(map(int, input().split()))
li.sort()
ref = 0
member = 1
for i in li :
	member += 1
	if member >= i :
		member = 0
		ref += 1
print(ref)