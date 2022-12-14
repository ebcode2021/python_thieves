# 배열의 크기 : n, 숫자가 더해지는 횟수 : m, 최대 연속 횟수 : k
n, m, k  = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

unit = array[len(array) - 1] * k + array[len(array) - 2]

unit_cnt = m // (k + 1)
remainder = m % (k + 1)

print(unit * unit_cnt + remainder * array[len(array) - 1])
