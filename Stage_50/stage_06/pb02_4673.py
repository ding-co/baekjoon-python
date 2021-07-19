# 2. 셀프 넘버 (4673)

# 함수 d를 정의하여 문제를 해결해 봅시다.
# github: ding-co

# Constraint

total_set = set(range(1, 10000 + 1))
not_self_number_set = set()

for i in range(1, 10000 + 1):
    for element in str(i):
        i += int(element)
    not_self_number_set.add(i)

self_number_set = sorted(total_set - not_self_number_set)

for self_number in self_number_set:
    print(self_number)