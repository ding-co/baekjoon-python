# 5. 알람 시계 (2884)

# 시간 뺄셈 문제
# github: ding-co

# Constraint
# 0. input: 0 <= h <= 23 and 0 <= m <= 59

h, m = map(int, input().split())

if m < 45:
    h -= 1
    if h < 0:
        h = 23
    m = 60 - (45 - m)
else:
    m -= 45

print(h, m)