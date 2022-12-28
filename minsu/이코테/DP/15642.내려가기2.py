import sys
import copy
input = sys.stdin.readline
n = int(input())
max_map = []
for _ in range(0, n) :
	max_map.append(list(map(int, input().split())))
min_map = copy.deepcopy(max_map)
for i in range(1, n) :
	max_map[i][0] += max(max_map[i - 1][0], max_map[i - 1][1])
	min_map[i][0] += min(min_map[i - 1][0], min_map[i - 1][1])
	max_map[i][1] += max(max_map[i - 1][0], max_map[i - 1][1], max_map[i - 1][2])
	min_map[i][1] += min(min_map[i - 1][0], min_map[i - 1][1], min_map[i - 1][2])
	max_map[i][2] += max(max_map[i - 1][2], max_map[i - 1][1])
	min_map[i][2] += min(min_map[i - 1][2], min_map[i - 1][1])
print(max(max_map[n - 1]), min(min_map[n - 1]), sep=" ")
