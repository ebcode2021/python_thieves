n = int(input())
li = []
for _ in range(n) :
	i = int(input())
	li.append(i)
li.sort(reverse=True)
cnt = 1
max_ = 0
for i in li :
	if (max_ <= i * cnt) :
		max_ = i * cnt
	cnt += 1
print(max_)