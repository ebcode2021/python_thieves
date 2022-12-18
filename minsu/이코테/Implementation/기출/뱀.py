from dataclasses import dataclass

@dataclass
class bam:
	view: int = 1
	size: int = 1
	head = [1,1]
	tail = [1,1]

def rotate(a, b) :
	c = a + b
	if (c < 0) :
		return 3
	if (c > 3) :
		return c % 4
	return c
	

udlr = [[0, -1], [1, 0], [0, 1], [-1, 0]]

n = int(input())
applecnt = int(input())
applepos = []
for i in range(applecnt) :
	applepos.append(list(map(int, input().split())))
rotatecnt = int(input())
rotateinfo = []
for i in range(rotatecnt) :
	rotateinfo.append(list(input().split()))
time = 0
bodyq = []
next_head = (0, 0)
find = False
bodyq.insert(0, list(bam.head))
while True :
	for i in rotateinfo :
		if (int(i[0]) == time) :
			if (i[1] == 'D') :
				bam.view = rotate(bam.view, 1)
			elif(i[1] == 'L') :
				bam.view = rotate(bam.view, -1)
	flag = False
	next_head = list(map(int,(int(bam.head[0]) + int(udlr[bam.view][0]), int(bam.head[1]) + int(udlr[bam.view][1]))))
	for i in bodyq :
		if (next_head[0] == i[0] and next_head[1] == i[1]) :
			find = True
			break
	if (find):
		break
	bodyq.insert(0, list(next_head))
	if ((next_head[0] < 1 or next_head[0] > n) or (next_head[1] < 1 or next_head[1] > n)) :
		break
	for i in applepos :
		if (next_head[1] == i[0] and next_head[0] == i[1]) :
			flag = True
			list.remove(applepos, i)
	if (flag == False and len(bodyq) > 0) :
		bodyq.pop()
	bam.head[0] = next_head[0]
	bam.head[1] = next_head[1]
	time+=1
print(time + 1)

