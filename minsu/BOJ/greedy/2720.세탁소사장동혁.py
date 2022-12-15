data = list(map(int, [25, 10, 5, 1]))
n = int(input())
for i in range(n) :
	num = int(input())
	for i in data :
		print(num // i, end=" ")
		num %= i