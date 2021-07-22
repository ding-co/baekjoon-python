# 8. 다이얼 (5622)

# 규칙에 따라 문자에 대응하는 수를 출력하는 문제

# github: ding-co

# Constraint
# 0. input: 2 <= len(word) <= 15, upper case word

input_data = input()

phone_alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
phone_time = [3, 4, 5, 6, 7, 8, 9, 10]

result_time = 0
for data in input_data:
    for i in range(len(phone_alphabet)):
        if data in phone_alphabet[i]:
            result_time += phone_time[i]

print(result_time)