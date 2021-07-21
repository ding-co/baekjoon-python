# 3. 알파벳 찾기 (10809)

# 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

# github: ding-co

# Constraint
# 0. input: 0 <= len(S) <= 100

input_data = input()
alphabet = [-1] * 26

for i in range(len(input_data)):
    if ord('a') <= ord(input_data[i]) <= ord('z') and \
        alphabet[ord(input_data[i]) - ord('a')] == -1 :
        alphabet[ord(input_data[i]) - ord('a')] += (i + 1)

print(*alphabet)