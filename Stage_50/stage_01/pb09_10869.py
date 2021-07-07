# 9. 사칙연산 (10869)

# 모든 연산 문제

a, b = map(int, input().split())

if (0 <= a <= 10000) and (0 <= b <= 10000):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)