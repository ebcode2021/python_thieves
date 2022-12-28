import sys

f = sys.stdin.readline

test = int(f())

res = []
def func(n, m, gold) :
	for col in range(1, m) :
		for row in range(n) :
			if row == 0 :
				gold[col + m * row] += max(gold[(col - 1) + m * row], gold[(col - 1) + m * (row + 1)])
			elif row == n - 1 :
				gold[col + m * row] += max(gold[(col - 1) + m * row], gold[(col - 1) + m * (row - 1)])
			else :
				gold[col + m * row] += max(gold[(col - 1) + m * row], gold[(col - 1) + m * (row + 1)], gold[(col - 1) + m * (row - 1)])
	return max(gold)

for _ in range(test) :
	n, m = map(int, f().split())
	gold = list(map(int, f().split()))
	res.append(func(n, m, gold))

print(*res, sep="\n")