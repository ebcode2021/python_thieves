N = int(input())
valueList = list(map(int, input().split()))

valueList.sort()
idx = 0
str_cnt = 0
g_cnt = 0
fear = 0
# while N > idx :
#     # print(idx, fear, g_cnt, str_cnt)   
#     if idx >= N :
#         break
#     fear = valueList[idx]
#     if fear == 1 :
#         g_cnt += 1
#         idx += fear
#     elif fear >= 2 :
#         idx += 1
#         if fear == valueList[idx] :
#             str_cnt += 1
#         elif fear != valueList[idx] :
#             fear = valueList[idx]
#             str_cnt += 1
#         if fear == str_cnt :
#             g_cnt += 1
#             continue
#         idx += 1
while idx < N :
    fear = valueList[idx]
    str_cnt += 1
    idx += 1
    print(idx, fear, g_cnt, str_cnt)
    if fear == str_cnt :
        g_cnt += 1
        str_cnt = 0
        idx += 1
print(g_cnt)