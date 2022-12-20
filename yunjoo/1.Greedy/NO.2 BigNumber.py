N, M, K = map(int, input().split())
sumList = list(map(int, input().split()))
sumList.sort(reverse=True)
answer = 0
cnt = 0
for i in range(M):
  if cnt != K:
    answer += int(sumList[0])
    cnt += 1
  elif cnt == K:
    answer += int(sumList[1])
    cnt = 0
print(answer)