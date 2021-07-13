# 9. 별 찍기 - 1 (2438)

# 별을 찍는 문제 1
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 100 (number ot stars)

n = int(input())

for i in range(1, n + 1):
    print("*" * i)