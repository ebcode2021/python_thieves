N, M = map(int, input().split())
weightList = list(map(int, input().split()))
weightList.sort()
cnt = 0
for i in range(N-1) :
    for j in range(i + 1, N) :
        if weightList[i] != weightList[j] :
            cnt += 1
print(cnt)