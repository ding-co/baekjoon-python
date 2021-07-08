# 11. 곱셈 (2588)

# 빈 칸에 들어갈 수는?

# Constraint
# 1. input => two three-digit natural numbers

num1 = input()
num2 = input()

multiply_1_digit = int(num1) * int(num2[-1])
multiply_10_digit = int(num1) * int(num2[-2])
multiply_100_digit = int(num1) * int(num2[-3])

result = multiply_1_digit + multiply_10_digit * 10 + multiply_100_digit * 100

print(multiply_1_digit)
print(multiply_10_digit)
print(multiply_100_digit)
print(result)
