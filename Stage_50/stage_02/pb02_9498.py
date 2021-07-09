# 2. 시험 성적 (9498)

# 시험 점수를 성적으로 바꾸는 문제
# github: ding-co

# Constraint
# 1. 0 <= 시험 점수 <= 100

test_score = int(input())

if 90 <= test_score <= 100:
    print("A")
elif 80 <= test_score:
    print("B")
elif 70 <= test_score:
    print("C")
elif 60 <= test_score:
    print("D")
else:
    print("F")