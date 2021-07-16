# 5. 평균 (1546)

# 평균을 조작하는 문제
# github: ding-co

# Constraint
# 0. input: 0 <= n <= 1000
# 1. input: 0 < score <= 100

subject_n = int(input())
subject_score = list(map(int, input().split()))

max_score = max(subject_score)

new_sum = 0
for score in subject_score:
    new_score = score / max_score * 100
    new_sum += new_score

print(new_sum / subject_n)