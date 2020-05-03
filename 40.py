"""
소수점 뒤에 양의 정수를 차례대로 붙여 나가면 아래와 같은 무리수를 만들 수 있습니다.

0.123456789101112131415161718192021...

이 무리수의 소수점 아래 12번째 자리에는 1이 옵니다 (위에서 붉게 표시된 숫자).

소수점 아래 n번째 숫자를 dn이라고 했을 때, 아래 식의 값은 얼마입니까?

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def answer(n):
    string = '0.'
    for i in range(1, n + 1):
        string += str(i)

    l = len(str(n))
    result = 1
    for i in range(l):
        result *= int(string[(10 ** i) + 1])

    return result

print(answer(1000000))