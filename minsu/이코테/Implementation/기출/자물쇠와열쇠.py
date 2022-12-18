from dataclasses import dataclass
import copy

@dataclass
class keyinfo:
	x:int = None
	y:int = None
@dataclass
class lockinfo:
	x:int = None
	y:int = None


def rotated(a):
	n = len(a)
	m = len(a[0])
	result = [[0] * n for _ in range(m)]
	for i in range(n):
		for j in range(m):
			result[j][n-i-1] = a[i][j]
	print(result)
	return result

def solution(key, lock):
	key = list(key)
	lock = list(lock)
	keyinfo.x = len(key[0])
	keyinfo.y = len(key)
	lockinfo.x = len(lock[0])
	lockinfo.y = len(lock)
	for _ in range(0, 4) :
		for y in range(0, lockinfo.y + keyinfo.y) :
			for x in range(0, lockinfo.x + keyinfo.x) :
				temp = copy.deepcopy(lock)
				ycnt = 0
				for loopy in range(y - keyinfo.y, y) :
					if (loopy >= 0 and loopy < lockinfo.y) :
						xcnt = 0
						for loopx in range(x - keyinfo.x, x) :
							if (loopx >= 0 and loopx < lockinfo.x) :
								temp[loopy][loopx] = lock[loopy][loopx] + key[ycnt][xcnt]
							xcnt += 1
					ycnt += 1
				check = True
				for i in temp :
					for k in i :
						if (k != 1) :
							check = False
							break
				if (check) : return True
		key = rotated(key)
	return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))