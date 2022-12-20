# 다시 풀기
import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n) :
	data = sys.stdin.readline().split()
	command = data[0]

	if len(data) > 1:
		num = int(data[1])

	if command == 'add' :
		s.add(num)
	elif command == 'remove' :
		s.discard(num)
	elif command == 'check' :
		print (1 if num in s else 0)
	elif command == 'toggle' :
		if num in s :
			s.discard(num)
		else :
			s.add(num)
	elif command == 'all' :
		s = set([i for i in range(1, 21)])
	else :
		s = set()
