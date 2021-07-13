# 10. 별 찍기 - 2 (2439)

# 별을 찍는 문제 2
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 100 (number of stars)

# My Solution 1

n = int(input())

for i in range(1, n + 1):
    print((" " * (n - i)), ("*" * i), sep="")

# My Solution 2

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(" ", end = "")
#     for k in range(1, i + 1):
#         print("*", end = "")
#     print()