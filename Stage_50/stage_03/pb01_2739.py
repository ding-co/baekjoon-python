# 1. 구구단 (2739)

# 구구단을 출력하는 문제
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 9

n = int(input())

for i in range(1, 9 + 1):
    print(f'{n} * {i} = {n * i}')