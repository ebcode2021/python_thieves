# 다시 풀기

def solution(food_times, k):
    index = 0
    food_len = len(food_times)
    
    if sum(food_times) <= k :
        return (-1)
    
    while k > 0 :
        if food_times[index % food_len] != 0:
            food_times[index % food_len] -= 1
            k -= 1
        index += 1
    while food_times[index % food_len] == 0 :
        index += 1
    return ((index % food_len) + 1)