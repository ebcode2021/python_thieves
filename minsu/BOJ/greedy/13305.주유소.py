n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
ref = 0
n_price = 100000000000000
for i in range(0, n - 1) :
	if (n_price > price[i]) :
		n_price = price[i]
	ref += n_price * road[i]
print(ref)