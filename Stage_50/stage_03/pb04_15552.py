# 4. 빠른 A+B (15552)

# 빠르게 입력받고 출력하는 문제
# github: ding-co

# Constraint
# 0. input: number of testcases t (t <= 1,000,000)
# 1. input: 1 <= a, b <= 1000

import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    a, b = map(int, input().split())
    print(a + b)