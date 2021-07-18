# 1. 정수 N개의 합 (15596)

# 함수를 구현해 봅시다. (이 문제는 C, C++, Python, Java, Go만 지원합니다. 그 외의 언어를 사용하신다면 이 문제를 무시해 주세요.)
# github: ding-co

# Constraint
# 0. def solve(a: list) -> int
# 1. input: 0 <= a[i] <= 1,000,000
# 2. input: 1 <= n <= 3,000,000
# 3. return sum(a)

def solve(a: list) -> int:
    ans = 0
    for element in a:
        ans += element
    return ans