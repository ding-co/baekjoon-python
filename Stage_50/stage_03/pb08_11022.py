# 8. A+B - 8 (11022)

# A+B를 바로 위 문제보다 아름답게 출력하는 문제
# github: ding-co

# Constraint
# 0. input: t (number of test cases)
# 1. input: 0 < a, b < 10

import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(1, n + 1):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i, a, b, a + b))