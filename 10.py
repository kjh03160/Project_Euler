"""

10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?

"""

def answer(k):
    ans_list = [2]
    num = 3
    ans = 0
    while num < k:
        isP = True
        for i in ans_list:
            if num % i == 0:
                isP = False
                break
            # else:
            #     isP = isP & True
        if isP:
            ans_list.append(num)
            ans += num
        num += 1

    return ans

# print(answer(2000000))


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

a = 0
for i in prime_list(10000000):
    if i < 2000000:
        a += i
print(a)