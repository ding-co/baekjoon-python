# 6. A-B (1001)

# 두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제

a, b = map(int, input().split())

if (0 < a < 10) and (0 < b < 10):
    print(a - b)