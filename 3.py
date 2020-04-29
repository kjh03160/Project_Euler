"""
어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

600851475143의 소인수 중에서 가장 큰 수를 구하세요.
"""


def key(n):
    answer = 0
    i = 2
    while n != 1:
        if n % i == 0:
            n //= i
            answer = i
        i += 1
    return answer

print(key(600851475143))


################## 공부할 것 ###############
# 에라토스테네스의 체 알고리즘으로 다음 소수를 구한다
def SieveOfEratosthenes(primeNums):
    lastPrimeNum = primeNums[len(primeNums) - 1]
    num = lastPrimeNum + 1
    while True:
        isPrime = True

        # 시련의 시작 - 선대 소수들에게 나누어지면 죽음이다..
        for prime in primeNums:
            if num % prime == 0:
                isPrime = False

        # 이모든 시련을 통과하면 소수로 인정 받는다..!
        if isPrime == True:
            primeNums.append(num)
            break
        num += 1


# number = 600851475143
# primeNums = [2]
# while primeNums[len(primeNums) - 1] <= number:
#     # 더이상 안나누어질때까지 계속 나눈다.
#     if number % primeNums[len(primeNums) - 1] == 0:
#         number = number / primeNums[len(primeNums) - 1]
#     # 안나누어지면 다음 소수를 구한다.
#     else:
#         SieveOfEratosthenes(primeNums)
# print(primeNums[len(primeNums) - 1])

# number = 2000000
# primeNums = [2]
# while primeNums[-1] <= number:
#     SieveOfEratosthenes(primeNums)
# print(sum(primeNums))

def is_prime_num(num) :
    for i in range(2, int(num**0.5) + 1):
        if num % i==0:
            return False
    return True

def sum_prime_nums(range_to) :
    prime_sum = 2+3+5+7
    for num in range(7, range_to+1) :
        if num % 2 !=0 and num % 3 !=0 and num % 5 !=0 and num % 7 !=0 :    #sieve of Eratosthenes
            if is_prime_num(num) :
                prime_sum = prime_sum + num
        num += 2
    return prime_sum

print(sum_prime_nums(200000))