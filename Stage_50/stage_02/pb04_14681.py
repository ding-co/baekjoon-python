# 4. 사분면 고르기 (14681)

# 점이 어느 사분면에 있는지 알아내는 문제
# github: ding-co

# Constraint
# 0. input1: -1000 <= x <= 1000 and x != 0
# 1. input2: -1000 <= y <= 1000 and y != 0

x = int(input())
y = int(input())

if x > 0:
    print(1) if y > 0 else print(4)

else:
    print(2) if y > 0 else print(3)