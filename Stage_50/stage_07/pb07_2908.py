# 7. 상수 (2908)

# 숫자를 뒤집어서 비교하는 문제

# github: ding-co

# Constraint
# 0. input: 3 digit number, exclude 0

a, b = input().split()
a, b = int(''.join(list(reversed(a)))), int(''.join(list(reversed(b))))

print(max(a, b))