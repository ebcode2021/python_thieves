from dataclasses import dataclass

@dataclass
class keyinfo:
	x:int = None
	y:int = None
class lockinfo:
	x:int = None
	y:int = None

def solution(key, lock):
	keyinfo.x = len(key[0])
	keyinfo.y = len(key)
	lockinfo.x = len(lock[0])
	lockinfo.y = len(lock)
	for i in range(0, 3) :
		ref = True
		for y in range(0, lockinfo.y) :
			for x in range(0, lockinfo.x) :
				ycnt = keyinfo.y
				for loopy in range(y - keyinfo.y, y) :
					if (loopy >= 0 and loopy < lockinfo.y) :
						xcnt = keyinfo.x
						for loopx in range(x - keyinfo.x, x) :
							if (loopx >= 0 and loopx < keyinfo.x) :
								if (key[ycnt][xcnt] != lockinfo[loopy][loopx]) :
									ref = False
									print(key[ycnt][xcnt], key[loopy][loopx])
									break
							xcnt -= 1
					if (ref == True) :
						return True
					ycnt -= 1
		#key = list(zip(key[::-1]))
	return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))