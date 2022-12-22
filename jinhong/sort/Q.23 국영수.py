import sys

N = int(sys.stdin.readline())
students = []
for i in range(N):
	name, korean, english, math = sys.stdin.readline().split()
	students.append([name, int(korean), int(english), int(math)])
students.sort(key=lambda student:(-student[1], student[2], -student[3], student[0]))
for student in students:
	print(student[0])