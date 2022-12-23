import sys

def bs(n, li, s, e) :
	if s > e :
		return "no"
	mid = (s + e) // 2
	if li[mid] == n :
		return "yes"
	if li[mid] < n :
		return bs(n, li, mid + 1, e)
	if li[mid] > n :
		return bs(n, li, s, mid - 1)

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
fi = list(map(int, sys.stdin.readline().split()))
for i in fi :
	print(bs(i, li, 0, n - 1), end=' ')