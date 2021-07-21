# 4. 문자열 반복 (2675)

# 각 문자를 반복하여 출력하는 문제

# github: ding-co

# Constraint
# 0. input: 1 <= test case numbers <= 1,000
# 1. input: 1 <= R <= 8, 1 <= len(S) <= 20

test_case_numbers = int(input())

for _ in range(test_case_numbers):
    r, string_data = input().split()
    for s in string_data:
        print(s * int(r), end = "")
    print()