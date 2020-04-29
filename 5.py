"""

1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

"""
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b is 0:
        return a
    if a % b is 0:
        return b
    return gcd(b, a % b)


def answer(k):
    ans = k
    for i in range(k, 1, -1):
        val = gcd(i, ans)
        if val == 1:
            ans *= i
        elif i % val == 0 and i != val:
            ans *= i // val
    return ans

print(answer(20))


