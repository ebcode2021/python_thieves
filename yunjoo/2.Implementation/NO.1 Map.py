N = int(input())
arr = list(input().split())
x = 1
y = 1
for walk in arr :
    if walk == 'R' and x + 1 <= N :
        x += 1
    elif walk == 'L' and x - 1 > 0 :
        x -= 1
    elif walk == 'U' and y - 1 > 0 :
        y -= 1
    elif walk == 'D' and y + 1 <= 5:
        y += 1
print(y, x)
