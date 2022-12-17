# 다시 풀기

strings = list(input())

strings.sort(key=lambda x : ord(x))
idx, num = 0, 0

for string in strings :
	if not(string >= '0' and string <= '9') :
		break
	num += int(string)
	idx += 1

if idx :
	print(''.join(strings[idx:]) + str(num))
else :
	print(''.join(strings))

