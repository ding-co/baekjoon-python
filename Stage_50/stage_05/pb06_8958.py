# 6. OX퀴즈 (8958)

# OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
# github: ding-co

# Constraint
# 0. input: test case number
# 1. input: 0 < len(test case) < 80

test_case_number = int(input())

for _ in range(test_case_number):
    score = 0
    test_case = input().split("X")
    for test in test_case:
        score += sum( [i for i in range(1, len(test) + 1)] )
    print(score)