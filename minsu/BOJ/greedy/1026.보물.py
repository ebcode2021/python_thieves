n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)
ref = 0
for i in range(0, n) :
	ref += arr1[i] * arr2[i] 
print(ref)