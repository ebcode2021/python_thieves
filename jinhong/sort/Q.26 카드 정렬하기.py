import sys

N = int(sys.stdin.readline())
cards = []
for _ in range(N):
	cards.append(int(sys.stdin.readline()))
cards.sort(reverse=True)
answer = cards[0] if N == 1 else 0
while len(cards) != 1:
	new_card = cards.pop() + cards.pop()
	answer += new_card
	cards.append(new_card)
print(answer)