# 1. A+B - 5 (10952)

# 0 0이 들어올 때까지 A+B를 출력하는 문제
# github: ding-co

# Constraint
# 0. input: 0 <a, b < 10

import sys

input = sys.stdin.readline

a, b = -1, -1

while a != 0 or b != 0:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)