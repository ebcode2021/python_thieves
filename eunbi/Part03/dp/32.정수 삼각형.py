import sys

f = sys.stdin.readline

row = int(f())
triangle = []

for _ in range(row) :
	triangle.append(list(map(int, f().split())))

for i in range(1, row) :
	for j in range(i + 1) :
		if j == 0 :
			triangle[i][j] += triangle[i-1][j]
		elif j == i :
			triangle[i][j] += triangle[i-1][j-1]
		else :
			triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
print(max(triangle[row -1]))
