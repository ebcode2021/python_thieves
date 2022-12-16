data = input()

middle = len(data) // 2
last = len(data)

left = 0
right = 0
for i in range(last) :
	if i < middle :
		left += int(data[i])
	else :
		right += int(data[i])
if (left == right) :
	print("LUCKY")
else :
	print("READY")

# another solve

data = input()
data_len = len(data)
sum = 0

for i in range(data_len // 2) :
    sum += int(data[i])

for i in range(data_len // 2, data_len) :
    sum -= int(data[i])

if (sum == 0) :
    print("LUCKY")
else :
    print("READY") 