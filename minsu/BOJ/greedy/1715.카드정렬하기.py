from heapq import heappush, heappop

n = int(input())
if (n == 1) :
	print(0)
	exit()
heap = []
for _ in range(n):
	i = int(input())
	heappush(heap, i)
ref = 0
sum_ = 0
while True :
	sum_ = heappop(heap) + heappop(heap)
	ref += sum_
	if (len(heap) == 0) :
		break
	heappush(heap, sum_)
print(ref)