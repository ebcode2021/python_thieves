import sys
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())), reverse= True)
print(arr[n // 2])