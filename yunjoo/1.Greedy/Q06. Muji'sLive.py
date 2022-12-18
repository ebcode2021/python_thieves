import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    # Queue에 순서대로 섭취소요 시간, 인덱스 추가
    # 섭취소요 시간이 적은 순서대로가 아닌 입력된 순서대로?
    que = []
    for i in range(len(food_times)):
        heapq.heappush(que, (food_times[i], i + 1))
    
    sum_value = 0            # 먹기 위해 사용한 시간
    previous = 0             # 직전에 다 먹은 음식 시간 
    length = len(food_times) # 남은 음식의 개수

    while sum_value + ((que[0][0] - previous) * length) <= k :
        print(que)
        now = heapq.heappop(que)[0]
        print("privious : " + str(previous) + " now : " + str(now))
        sum_value += (now - previous) * length
        print("sum value : " + str(sum_value) + " length : " + str(length))
        length -= 1 # 다 먹은 음식 제외
        previous = now

    result = sorted(que, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]


food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times, k))

#다시 풀기!
# food_times = list(map(int, input().split()))
# k = int(input())
# time = 0
# answer = 0
# arr_len = len(food_times)
# while time <= k + 1 :
#     for idx in range(arr_len) :
#         if food_times[idx] == 0 :
#             continue
#         food_times[idx] -= 1
#         time += 1
#         if time == k + 1 :
#             print(idx + 1)


