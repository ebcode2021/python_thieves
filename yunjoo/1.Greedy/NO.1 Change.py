coinList = [500, 100, 50, 10]
N = int(input())
cnt = 0
for coin in coinList :
    cnt += N // coin
    N %= coin
print(cnt)