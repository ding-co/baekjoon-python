# 5. N 찍기 (2741)

# 1부터 N까지 출력하는 문제
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 100,000

import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(1, n + 1):
    print(i)