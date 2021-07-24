# 9. 크로아티아 알파벳 (2941)

# 크로아티아 알파벳의 개수를 세는 문제

# github: ding-co

# Constraint
# maximum length 100, alphabet lower case, '-', '='
# word consists of croatia alphabet

croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

input_data = input()

for alphabet in croatia_alphabet:
  input_data = input_data.replace(alphabet, "_")

print(len(input_data))