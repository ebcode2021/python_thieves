import sys

N = int(sys.stdin.readline())
students = []
for _ in range(N):
	name, score = sys.stdin.readline().split()
	students.append((name, int(score)))
students.sort(key=lambda x:x[1])
for name, score in students:
	print(name, end=" ")
print()