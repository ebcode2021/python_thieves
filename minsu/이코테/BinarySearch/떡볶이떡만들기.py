import sys

freddy = sys.stdin.readline

_i, i_ = map(int, freddy().split())
_minsu = list(map(int, freddy().split()))
sTarT = 0
eNd = max(_minsu) - 1
pikachu = 0
while sTarT <= eNd :
	asdf = (eNd + sTarT) // 2
	qwer = 0
	for abc in _minsu : 
		if abc > asdf : qwer += abc - asdf
	if qwer >= i_ : 
		sTarT = asdf + 1
		pikachu = asdf
	else : eNd = asdf - 1
print(pikachu)
