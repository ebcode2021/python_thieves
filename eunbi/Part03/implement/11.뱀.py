## 다시풀기..

# n : board 의 크기
n = int(input())
apple_cnt = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

# board 데이터 세팅 (0 : 아무 것도 없음, 1 : 뱀의 몸통 위치, 2 : 사과 위치)
board[1][1] = 1
for _ in range(apple_cnt) :
    i, j = map(int, input().split())
    board[i][j] = 2

# 뱀의 예정된 회전 정보 저장
rotation_cnt = int(input())
rotation_lists = []
direction_lists = []
for _ in range(rotation_cnt) :
    sec, direction = map(str, input().split())
    rotation_lists.append(int(sec))
    direction_lists.append(direction)

# 회전 할 시,  동 남 서 북
x_direct = [0, 1, 0, -1]
y_direct = [1, 0, -1, 0]

# 시작 시점 및 위치 세팅
my_sec, idx = 0, 0
my_x, my_y = 1, 1
route_lists = [[1, 1], ]

def check_position(my_x, my_y) :
    # 범위 밖에 도달하거나
    if my_x < 1 or my_y < 1 or my_x > n or my_y > n :
        return (0)
    # 자기 몸에 닿거나
    if board[my_x][my_y] == 1 :
        return (0)
    return (1)

def check_rotation(idx) :
    # 회전 키워드 확인
    if direction_lists[0] == 'L' :
        idx -= 1
    else :
        idx += 1
    # 인덱스 오버될 경우 인덱스 조정
    if idx > 3 :
        idx -= 4
    elif idx < 0 :
        idx += 4
    # 첫번째 리스트 삭제
    del direction_lists[0]
    return (idx)

while True :
    if my_sec in rotation_lists :
        idx = check_rotation(idx)
    my_x += x_direct[idx]
    my_y += y_direct[idx]
    my_sec += 1
    if not check_position(my_x, my_y) :
        break
    route_lists.append([my_x, my_y])
    if board[my_x][my_y] != 2 :
        board[route_lists[0][0]][route_lists[0][1]] = 0
        del route_lists[0]
    board[my_x][my_y] = 1

print(my_sec)