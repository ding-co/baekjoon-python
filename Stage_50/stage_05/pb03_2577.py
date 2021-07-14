# 3. 숫자의 개수 (2577)

# 각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제
# github: ding-co

# Constraint
# 0. input: 100 <= a, b, c <= 1000

a = int(input())
b = int(input())
c = int(input())

result_list = [0] * 10

for i in str(a * b * c):
    result_list[int(i)] += 1

print(*result_list, sep = "\n")