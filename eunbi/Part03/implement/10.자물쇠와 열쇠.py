#### 다시 풀기

def rotate(key) :
	reversed_ = key[::-1]
	rotated = list(zip(*reversed_))
	return (rotated)

# def rotate(key) :
# 	n = len(key)
# 	m = len(key[0])
# 	res = [[0] * n for _ in range(m)]
# 	for i in range(n) :
# 		for j in range(m) :
# 			res[j][n-i-1] = key[i][j]
# 	return res

def check(new_lock) :
	lock_length = len(new_lock) // 3
	for i in range(lock_length, lock_length * 2) :
		for j in range(lock_length, lock_length * 2) :
			if new_lock[i][j] != 1 :
				return False
	return True

def solution(key, lock) :
	n = len(lock)
	m = len(key)
	# 자물쇠의 크기를 3배로 변환
	new_lock = [[0] * (n * 3) for _ in range(n * 3)]
	for i in range(n) :
		for j in range(n) :
			new_lock[i + n][j + n] = lock[i][j]
	
	for rotation in range(4) :
		key = rotate(key)
		for x in range(n * 2) :
			for y in range(n * 2) :
				for i in range(m) :
					for j in range(m) :
						new_lock[x + i][y + i] += key[i][j]
				if check(new_lock) == True :
					return True
				for i in range(m) :
					for j in range(m) :
						new_lock[x + i][y + j] -= key[i][j]
	return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))