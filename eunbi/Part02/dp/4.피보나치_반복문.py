# DP 테이블(저장용 리스트) 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# bottom-up 방식
for i in range(3, n + 1) :
	d[i] = d[i - 1] + d[i - 2]

print(d[n])