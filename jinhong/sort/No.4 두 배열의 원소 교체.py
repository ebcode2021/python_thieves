N, K = map(int, input().split())
A = [int(num) for num in input().split()]
B = [int(num) for num in input().split()]
A.sort()
B.sort(reverse=True)
for i in range(K):
	if (A[i] > B[i]):
		break
	A[i], B[i] = B[i], A[i]
print(sum(A))