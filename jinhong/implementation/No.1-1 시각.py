Time = int(input())
hour, min, sec = 0, 0, 0
answer = 0
while hour < Time + 1:
	time = str(hour) + str(min) + str(sec)
	if '3' in time:
		answer += 1
	sec += 1
	if sec == 60:
		sec = 0
		min += 1
	if min == 60:
		min = 0
		hour += 1
print(answer)
