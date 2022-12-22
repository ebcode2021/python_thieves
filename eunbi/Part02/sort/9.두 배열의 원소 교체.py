import sys

f = sys.stdin.readline

lst_cnt, change_cnt= map(int, f().split())
lst_a = []
lst_b = []

lst_a = list(map(int, f().split()))
lst_b = list(map(int, f().split()))

lst_a.sort()
lst_b.sort()

idx = 0
max_idx = len(lst_a) - 1
while change_cnt:
	if (lst_a[idx] < lst_b[max_idx - idx]) :
		lst_a[idx], lst_b[max_idx - idx] = lst_b[max_idx - idx], lst_a[idx]
	else :
		break
	idx += 1
	change_cnt -= 1
print(sum(lst_a))
