"""
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요.
"""

def answer(k):
    ans_list = [2]
    num = 3

    while len(ans_list) < k:
        isP = True
        for i in ans_list:
            if num % i == 0:
                isP = False

            else:
                isP = isP & True
        if isP:
            ans_list.append(num)
        num += 1

    return ans_list[-1]

print(answer(10001))

