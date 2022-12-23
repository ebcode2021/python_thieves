import sys

f = sys.stdin.readline

owner = int(f())
storage = sorted(list(map(int, f().split())))
storage_len = len(storage)

client = int(f())
orders = list(map(int, f().split()))

def binary_search(storage, target, start, end) :

	while start <= end :
		mid = (start + end) // 2
		if storage[mid] == target :
			return mid
		elif storage[mid] > target :
			end = mid - 1
		else :
			start = mid + 1
	return None

for order in orders :
	output = binary_search(storage, order, 0, storage_len - 1)
	if output != None :
		print("yes", end=" ")
	else :
		print("no", end=" ")

