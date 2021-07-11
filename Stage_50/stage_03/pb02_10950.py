# 2. A+B - 3 (10950)

# A+B를 여러 번 출력하는 문제
# github: ding-co

# Constraint
# 0. input: number of test cases T
# 1. input: 0 < A, B < 10

import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)