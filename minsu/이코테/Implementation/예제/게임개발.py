from dataclasses import dataclass

@dataclass
class character:
	x:int = None
	y:int = None
	view:int = None
@dataclass
class left:
	x:int = None
	y:int = None

def leftturn() :
	character.view -= 1
	if (character.view == -1) : character.view = 3

mapinfo = list(map(int, input().split()))
character.x, character.y, character.view = (map(int, input().split()))
ewsn = [[0, -1], [1, 0], [0 ,1], [-1, 0]]
map_ = []
for i in range(mapinfo[0]) :
	map_.append(list(map(int, input().split())))
ref = 0
while True : 
	cnt = 0
	while cnt < 4 :
		leftturn()
		left.x = character.x + ewsn[character.view][0]
		left.y = character.y + ewsn[character.view][1]
		if (left.x >= 0 and left.x < mapinfo[1] and left.y >= 0 and left.y < mapinfo[0]) : 
			if (map_[left.y][left.x] == 0) :
				ref += 1
				map_[left.y][left.x] = 3
				character.x = left.x
				character.y = left.y
				break
		cnt += 1
	if (cnt == 4) :
		tmp = character.view
		leftturn()
		leftturn()
		left.x = character.x + ewsn[character.view][0]
		left.y = character.y + ewsn[character.view][1]
		if (left.x >= 0 and left.x < mapinfo[1] and left.y >= 0 and left.y < mapinfo[0]) :
			if (map_[left.y][left.x] == 1) :
				break
			else :
				character.x = left.x
			character.y = left.y
			character.view = tmp
		else :
			break
print(ref)

