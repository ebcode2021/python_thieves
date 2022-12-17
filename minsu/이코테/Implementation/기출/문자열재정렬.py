import re
li = input()
ref = 0
for i in li :
	if (str.isdigit(i)) :
		ref += int(i)
li = re.sub("[0-9]", "", li)
li = ''.join(sorted(li))
print(li + str(ref))