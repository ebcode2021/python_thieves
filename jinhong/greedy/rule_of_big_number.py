answer = 0
arr_len, iter, max_repeat = map(int, input().split())
arr = sorted([int(i) for i in input().split()], reverse=True)
repeat = 0
for _ in range(iter):
	if repeat == max_repeat:
		repeat = 0
		answer += arr[1]
	else:
		answer += arr[0]
		repeat += 1
print(answer)