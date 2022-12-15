data = list(map(int, [500, 100, 50, 10, 5, 1]))
n = 1000 - int(input())
ref = 0
for i in data :
	ref += n // i
	n %= i 
print(ref)