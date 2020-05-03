"""
대칭수(palindrome)인 585는 2진수로 나타내도 10010010012가 되어 여전히 대칭수입니다.

10진법과 2진법으로 모두 대칭수인 1,000,000 이하 숫자의 합을 구하세요.

(주의: 첫번째 자리가 0이면 대칭수가 아님)
"""

def answer(k):
    result = []

    for x in range(1, 10):
        srting = str(bin(x))[2:]
        isA = True
        for o in range((len(srting) // 2)):
            if srting[o] != srting[(len(srting) - 1 - o)]:
                isA = False
                break

        if isA:
            result.append(x)

    for i in range(10, k + 1):
        string = str(i)
        binary = str(bin(i))[2:]
        isA = True
        for k in range((len(string) // 2)):
            if string[k] != string[(len(string) - 1 - k)]:
                isA = False
                break

        for j in range((len(binary) // 2)):
            if binary[j] != binary[(len(binary) - 1 - j)]:
                isA = isA & False
                break
        if isA:
            result.append(i)
    print(result)
    return sum(result)

print((answer(1000000)))