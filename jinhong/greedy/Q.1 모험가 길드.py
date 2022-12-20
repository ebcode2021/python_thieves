answer = 0
number_of_adventurers = int(input())
adventurers = sorted([int(i) for i in input().split()], reverse=True)
group = []
while adventurers:
	group.append(adventurers.pop())
	if len(group) == max(group):
		answer += 1
		group = []
print(answer)