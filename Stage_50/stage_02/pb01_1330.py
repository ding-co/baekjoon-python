# 1. 두 수 비교하기 (1330)

# 두 수를 비교한 결과를 출력하는 문제
# github: ding-co

# Constraint
# 1. -10,000 <= a, b <= 10,000

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")