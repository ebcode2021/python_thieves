import sys
from bisect import bisect_left, bisect_right

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left = bisect_left(arr, m)
right = bisect_right(arr, m)
if (right - left == 0) :
	print(-1)
else :
	print(right - left)