"""
2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

2 ** 1000의 각 자리수를 모두 더하면 얼마입니까?
"""

def answer(n):
    k = 2
    for i in range(1, n):
        k *= 2
    return sum(list(map(int, str(k))))

print(answer(1000))