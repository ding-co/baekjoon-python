# 2. A+B - 4 (10951)

# 입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.
# github: ding-co

# Constraint
# 0. input: 0 < a, b < 10

import sys

input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break