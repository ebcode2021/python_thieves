n = int(input())
li = list(map(int, input().split()))
x = 1
li.sort()
for i in li :
	if (x < i) :
		break
	x += i
print(x)