# *** 3. 더하기 사이클 (1110) ***

# 원래 수로 돌아올 때까지 연산을 반복하는 문제
# github: ding-co

# Constraint
# 0. input: 0 <= n <= 99

n = input()

temp = n
count = 0

while True:
    if len(temp) == 1:
        temp = "0" + temp
    
    temp = temp[-1] + str((int(temp[0]) + int(temp[1])) % 10)
    count += 1

    if int(n) == int(temp):
        break

print(count)