# 다시풀기!
N = int(input())
coinList = list(map(int, input().split()))
coinList.sort()

target = 1
for coin in coinList:
    if target < coin :
        break
    target += coin
    print(target)
print(target)