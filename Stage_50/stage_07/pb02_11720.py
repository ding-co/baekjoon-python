# 2. 숫자의 합 (11720)

# 정수를 문자열로 입력받는 문제. 
# Python처럼 정수 크기에 제한이 없다면 상관 없으나, 
# 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.

# github: ding-co

# Constraint
# 0. input: 1 <= N <= 100
# 1. input: N numbers

n = int(input())
input_data = input()

sum = 0
for data in input_data:
    sum += int(data)

print(sum)