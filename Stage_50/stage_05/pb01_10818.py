# 1. 최소, 최대 (10818)

# 최솟값과 최댓값을 찾는 문제
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 1,000,000
# 1. input: -1,000,000 <= all n numbers <= 1,000,000

n = int(input())
input_list = list(map(int, input().split()))

min_value = input_list[0]
max_value = input_list[0]

for i in range(len(input_list)):
    if input_list[i] < min_value:
        min_value = input_list[i]

for element in input_list:
    if element > max_value:
        max_value = element

print(min_value, max_value)