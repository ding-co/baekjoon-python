# 3. 합 (8393)

# 1부터 N까지의 합을 구하는 문제. 물론 반복문 없이 풀 수도 있습니다.
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 10000

import sys

input = sys.stdin.readline

n = int(input().rstrip())

result = 0

for i in range(1, n + 1):
    result += i

print(result)

# Reference: Not use 'for loop' statement
# print(sum(range(1, n + 1)))