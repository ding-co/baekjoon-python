# 3. 윤년 (2753)

# 윤년을 판별하는 문제
# github: ding-co

# Constraint
# 1. 1 <= 연도 <= 4000 (natural number)

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(1)
else:
    print(0)