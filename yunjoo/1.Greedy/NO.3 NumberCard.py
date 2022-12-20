N, M = map(int, input().split())
cardList = []
minList = []
for i in range(N):
    cardList.append(list(map(int, input().split())))
    minList.append(min(cardList[i]))
print(max(minList))