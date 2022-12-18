N, M = map(int, input().split())
answer = 0
while True :
    if N == 1:
        break;
    if N % M == 0:
        N = N // M
        answer += 1
    else:
        N = N - 1
        answer += 1
print(answer)