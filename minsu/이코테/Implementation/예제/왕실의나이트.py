pos = list(input())
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
movd = [
	(-2, +1),
	(-2, -1),
	(+2, -1),
	(+2, +1),
	(+1, +2),
	(-1, +2),
	(+1, -2),
	(-1, -2)
]
x = int(dic[pos[0]])
y = int(pos[1])
cnt = 0
for i in movd :
	if (x + i[0] >= 1 and x + i[0] <= 8 and y + i[1] >= 1 and y + i[1] <= 8) :
		cnt += 1
print(cnt)