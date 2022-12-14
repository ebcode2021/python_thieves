import heapq
import sys

n = int(input())
card_deck = []
for _ in range(n) :
	heapq.heappush(card_deck, int(sys.stdin.readline()))

if len(card_deck) == 1 :
	print(0)
else :
	answer = 0
	while len(card_deck) > 1 :
		tmp1 = heapq.heappop(card_deck)
		tmp2 = heapq.heappop(card_deck)
		answer += tmp1 + tmp2
		heapq.heappush(card_deck, tmp1 + tmp2)
	print(answer)



#
# heapq 
# -> 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
# -> 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은 값은 언제나 인덱스 0. 이진 트리의 루트에 위치.
#
#
#  #



########### (wrong code) : 시간 복잡도를 고려하지 않고 짬
cnt = int(input())

cards = list()
for _ in range(cnt) :
	cards.append(int(input()))

cards.sort()

res = 0

if (cnt == 1) :
	print(0)
else :
	while len(cards) != 1 :
		tmp_list = list()
		for i in range (0, len(cards) // 2) :
			tmp_list.append(cards[2 * i] + cards[2 * i + 1])
			res += cards[2 * i] + cards[2 * i + 1]
		if (len(cards) % 2) :
			tmp_list.append(cards[len(cards) - 1])
		tmp_list.sort()
		cards = tmp_list
	print(res)
