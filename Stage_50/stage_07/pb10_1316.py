# 10. 그룹 단어 체커 (1316)

# 조건에 맞는 문자열을 찾는 문제

# github: ding-co

# Constraint
# 0. input: 1 <= N <= 100
# 1. N lines - word, len(word) <= 100, lower case

n = int(input())

result = n

for _ in range(n):
  input_word = input()
  for j in range(len(input_word) - 1):
    if input_word[j] != input_word[j + 1]:
      if input_word[j] in input_word[j+1:]:
        result -= 1
        break

print(result)