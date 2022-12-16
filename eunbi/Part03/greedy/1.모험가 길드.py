n = int(input())
data = list(map(int, input().split()))

data.sort()

tmp = 1
res = 0
for i in range(n) :
	if data[i] > tmp :
		tmp += 1
	else :
		tmp = 1
		res += 1

print(res)

# another_solve
count = 0
result = 0
for i in data :
	count += 1
	if count >= i :
		count = 0
		result += 1
print(result)