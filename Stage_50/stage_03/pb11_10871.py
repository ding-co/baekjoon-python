# 11. X보다 작은 수 (10871)

# for와 if를 같이 쓰는 문제
# github: ding-co

# Constraint
# 0. input: sequence A (n numbers), int x
# 1. input: 1 <= n, x <= 10,000
# 2. input: 1 <= sequence elements <= 10,000

import sys

input = sys.stdin.readline

n, x = map(int, input().split())
seq = list(map(int, input().split()))

for element in seq:
    if element < x:
        print(element, end = " ")