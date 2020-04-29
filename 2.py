"""

피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

"""
def fib(n):
    fibList = [1, 1]

    if n == 1 or n == 2:
        return 1

    for i in range(2, n):
        fibList.append(fibList[i - 1] + fibList[i - 2])

    return fibList


sum = 0
for i in fib(40):
    if i % 2 == 0 and i <= 4000000:
        sum += i


print(sum)