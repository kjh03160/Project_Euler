"""
어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다. 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.

이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을 사전식(lexicographic) 순서라고 합니다.
0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.

012   021   102   120   201   210
0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째는 무엇입니까?
"""

def answer(k):
    strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    fact_list = [0]

    def fact(n):
        if n == 1:
            fact_list.append(1)
            return 1
        val = n * fact(n - 1)
        fact_list.append(val)
        return val
    fact(len(strings))

    find_ = k - 1
    start = 9
    div = fact_list[start]
    result_list = []

    while div:
        val = find_ // div
        result_list.append(strings[val])
        del strings[val]

        find_ = find_ % div
        start -= 1
        div = fact_list[start]

    return "".join(result_list + strings)

print(answer(1000000))

"""
1번째 숫자 : (찾으려는 순서 - 1) // fact(n-1)
2번째 숫자 : (위의 식의 나머지) // fact(n-2)
3번째 숫자 : (위의 식의 나머지) // fact(n-3)
4번째 숫자 : (위의 식의 나머지) // fact(n-4)
.
.
.
.
"""