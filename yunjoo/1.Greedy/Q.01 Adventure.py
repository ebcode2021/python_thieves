N = int(input())
valueList = list(map(int, input().split()))

valueList.sort()
idx = 0
str_cnt = 0
g_cnt = 0
fear = 0
while idx < N :
    fear = valueList[idx]
    str_cnt += 1
    idx += 1
    if fear == str_cnt :
        g_cnt += 1
        str_cnt = 0
print(g_cnt)