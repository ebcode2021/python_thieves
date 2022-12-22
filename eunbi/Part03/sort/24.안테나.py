import sys

f = sys.stdin.readline

n = int(f())
homes = list(map(int, f().split()))
homes.sort(reverse=True)
print(homes[n // 2])



