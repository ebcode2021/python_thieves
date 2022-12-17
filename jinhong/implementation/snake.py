from collections import deque

def move(head, heading):
	row, col = head[0], head[1]
	if heading == 0:
		return (row, col + 1) if col < N else (row, col)
	if heading == 90:
		return (row - 1, col) if row > 1 else (row, col)
	if heading == 180:
		return (row, col - 1) if col > 1 else (row, col)
	if heading == 270:
		return (row + 1, col) if row < N else (row, col)

def change_heading(heading, turn):
	if turn == 'L':
		heading = (heading + 90) % 360
	elif turn == 'D':
		heading = (heading + 270) % 360
	return heading

#Create a map
N = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]

#place apples
number_of_apples = int(input())
for _ in range(number_of_apples):
	apple = input().split()
	row, col = int(apple[0])-1, int(apple[1])-1
	map[row][col] = 1

#Create command list
commands = deque()
number_of_commands = int(input())
for _ in range(number_of_commands):
	command = input().split()
	commands.append((int(command[0]), command[1]))

#Initialize snake position and heading
snake = deque()
head = (1,1)
snake.append(head)
heading = 0
time = 0
next_command = commands.popleft()

while True:
	time += 1
	#Move snakes head 1 at a time
	next_position = move(head, heading)
	#Check if snake hits it own body or the wall
	if next_position in snake or head == next_position:
		print(time)
		break
	#Update state of snake
	head = next_position
	snake.appendleft(head)
	#Check if snake hits apple
	#Last tail position is reoved if not apple
	if map[head[0] - 1][head[1] - 1] == 1:
		map[head[0] - 1][head[1] - 1] = 0
	else:
		snake.pop()
	#Turn snakes head
	if time == next_command[0]:
		heading = change_heading(heading, next_command[1])
		if commands:
			next_command = commands.popleft()