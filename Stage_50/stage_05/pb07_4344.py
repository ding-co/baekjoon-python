# 3. 평균은 넘겠지 (4344)

# 과연 그럴까요?
# github: ding-co

# Constraint
# 0. input: test case number C
# 1. input: 1 <= student numbers N <= 1000
# 2. input: N scores, 0 <= score <= 100

test_case_number = int(input())
for _ in range(test_case_number):
    input_list = list(map(int, input().split()))
    student_number, student_scores = input_list[0], input_list[1:]

    student_avg = sum(student_scores) / student_number

    over_count = 0
    for student_score in student_scores:
        if student_score > student_avg:
            over_count += 1

    result = over_count / student_number * 100
    print("%.3f" % result, "%", sep = "")