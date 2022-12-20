string = input()
alphabets = ''
num = []
for c in string:
	if c.isalpha():
		alphabets += c
	else:
		num.append(int(c))
str_num = str(sum(num)) if num else ""
print(''.join(sorted(alphabets)) + str_num)