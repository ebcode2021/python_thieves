answer = 1
nums = input()
if nums == '0':
	print(0)
else:
	for num in nums:
		if num != '0':
			answer *= int(num)
	print(answer)