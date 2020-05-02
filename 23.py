"""
자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 초과수라고 합니다.

12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 초과수 중에서는 가장 작습니다.
따라서 초과수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 초과수의 합으로 표현 가능함을 보일 수가 있습니다.
두 초과수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

그렇다면, 초과수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?
"""
import math
def answer(n):
    excess_nums = []
    def is_excess(k ,list1):
        for i in range(1, k + 1):
            temp_list = []
            for x in range(1, int(math.sqrt(i)) + 1):
                if i % x == 0 and i != x:
                    temp_list.append(x)
                    temp_list.append(i // x)
            temp_list = set(sorted(temp_list)[:-1])
            if sum(temp_list) > i:
                list1.append(i)
    is_excess(n, excess_nums)
    print(excess_nums)

    result_set = set()
    for i in excess_nums:
        for k in excess_nums:
            if (i + k) < n:
                result_set.add(i + k)

    return sum(range(1, n)) - sum(result_set)

print(answer(28123))