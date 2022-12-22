import sys

N = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()
print(houses[N//2 - 1 + N%2])