# 5. 단어 공부 (1157)

# 단어의 개수를 구하는 문제

# github: ding-co

# Constraint
# 0. input: 1 <= len(word) <= 1,000,000

input_data = input().lower()
input_set = sorted(set(input_data))
input_count = [0] * len(input_set)

for data in input_data:
    if data in input_set:
        input_count[input_set.index(data)] += 1

if input_count.count(max(input_count)) == 1:
    print(input_set[input_count.index(max(input_count))].upper())
else:
    print("?")