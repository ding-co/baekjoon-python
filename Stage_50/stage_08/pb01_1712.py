# 1. 손익분기점 (1712)

# 이익이 발생하는 지점을 찾는 문제
# github: ding-co

# Constraint
# 0. input: 1 <= A, B, C <= 21 billion

a, b, c = map(int, input().split())

if (b-c) != 0:
    x = (-a)/(b-c)
    if x >= 0:
        print(int(x) + 1)
    else:
        print(-1)
else:
    print(-1)