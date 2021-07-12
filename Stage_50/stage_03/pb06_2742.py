# 6. 기찍 N (2742)

# 제문 는하력출 지까N 터부1
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 100,000

import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n, 0, -1):
    print(i)