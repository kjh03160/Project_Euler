"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""
def isPalin(x):
    p_list = []
    for i in range(10**(x - 1), 10**x):
        for j in range(10**(x - 1), 10**x):
            isP = str(i * j)
            bool = True
            for k in range(len(isP)):
                if isP[k] != isP[-(k + 1)]:
                    bool = False
                    break
            if bool:
                p_list.append(int(isP))

    return max(p_list)

print(isPalin(3))
