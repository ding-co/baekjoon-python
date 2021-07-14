# 4. 나머지 (3052)

# 위와 비슷한 문제
# github: ding-co

# Constraint
# 0. input: 0 <= number <= 1000

input_list = []

for _ in range(1, 10 + 1):
    num = int(input())
    num %= 42
    input_list.append(num)

print(len(set(input_list)))