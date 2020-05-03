"""
분자가 1인 분수를 단위분수라고 합니다. 분모가 2에서 10까지의 단위분수는 아래와 같습니다.


숫자 위에 찍힌 점은 순환마디를 나타내는데, 1/6의 경우 순환마디는 "6"으로 0.166666...처럼 6이 무한히 반복됨을 뜻합니다. 같은 식으로 1/7은 6자리의 순환마디(142857)를 가집니다.

d 를 1000 이하의 정수라고 할 때, 단위분수 1/d 의 순환마디가 가장 긴 수는 무엇입니까?
"""

def answer(d):
    remain_list = list()
    dividend = 1
    n = 0

    while True:
        remain = dividend % d  # 나머지
        # print(1 / d, remain_list, remain)
        if remain in remain_list:
            return n - remain_list.index(remain)
        else:
            remain_list.append(remain)
            dividend = remain * 10
            n += 1

    return remain_list

nums = [0, 0]
for i in range(2, 1000):
    nums.append(answer(i))
    # print(i, (answer(i)))

print(nums.index(max(nums)))