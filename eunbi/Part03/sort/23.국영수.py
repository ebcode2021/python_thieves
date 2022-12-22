import sys

f = sys.stdin.readline

n = int(f())

studnets = []
for _ in range(n) :
	name, korean, english, math = f().split()
	studnets.append([name, int(korean), int(english), int(math)])


studnets.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for student in studnets :
	print(student[0])