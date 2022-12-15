n = int(input())
li = list(map(int, input().split()))
n = 0
cnt = 0
for i in li :
	if (i == n) : 
		cnt += 1
		n += 1
		if (n == 3):
			n = 0
print(cnt)