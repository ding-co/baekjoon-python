# 3. 한수 (1065)

# X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다.
# github: ding-co

# Constraint
# 0. input: 1 <= n <= 1,000

n = int(input())

def hansu(n):
    result = 0
    for i in range(1, n + 1):
        if i <= 99:
            result += 1
        for j in range(2, len(str(i))):
            if int(str(i)[j]) - int(str(i)[j - 1]) \
                == int(str(i)[1]) - int(str(i)[0]):
                    result += 1
    return result

print(hansu(n))