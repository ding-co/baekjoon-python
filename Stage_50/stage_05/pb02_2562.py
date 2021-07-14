# 2. 최댓값 (2562)

# 최댓값이 어디에 있는지 찾는 문제
# github: ding-co

# Constraint

input_list = []

for _ in range(1, 9 + 1):
    num = int(input())
    input_list.append(num)

max_value = input_list[0]
for i in range(1, len(input_list) + 1):
    if input_list[i - 1] > max_value:
        max_value = input_list[i - 1]

print(max_value)
print(input_list.index(max_value) + 1)