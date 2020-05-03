"""
숫자 145에는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.

이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.

단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.
"""



def answer(k):
    fact = [1]
    x = 1
    for i in range(1, 10):
        x *= i
        fact.append(x)
    print(fact)
    nums = []
    for i in range(3, k + 1):
        val = 0
        for k in str(i):
            val += fact[int(k)]
        if i == val:
            nums.append(i)
    print(nums)
    return sum(nums)

print(answer(2540160))
print(362880 * 7)
print(9999999)