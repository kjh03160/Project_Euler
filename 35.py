"""
소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 circular prime이라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.

이런 소수는 100 밑으로 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.

그러면 1,000,000 밑으로는 모두 몇 개나 있을까요?
"""
import time

def answer(k):

    isP = [True] * k

    m = int(k ** 0.5)
    for i in range(2, m + 1):
        if isP[i] == True:           # i가 소수인 경우
            for j in range(i + i, k, i): # i이후 i의 배수들을 False 판정
                isP[j] = False

    primes = [i for i in range(2, k) if isP[i] == True]

    result = []

    for i in primes:
        if i <= 9:
            result.append(i)

        if i in result:
            continue

        string = list(str(i))
        boolean = True
        temp_nums = []

        for x in range(len(string) - 1):
            temp = list(string.pop())
            string = temp + string
            val = "".join(string)
            if int(val) not in primes:
                boolean = boolean & False
                break

            temp_nums.append(int(val))
            temp_nums.append(i)

        if boolean:
            result += temp_nums
    print(result)

    return len(set(result))

before = time.time()
print(answer(1000000))
now = time.time()
print(now - before, "secs")

def is_prime(num):
    if num == 1:
      return False
    if (num % 2 == 0 and num > 2):
       return False
    for i in range(3, int(num**0.5 + 1), 2):
        if num % i == 0:
            return False
    return True

def is_circular_prime(n):
  ns = str(n)
  ns2 = ns + ns # 문자열을 두 번 더한 문자열을 만든다
  for i in range(len(ns)):
    if not is_prime(int(ns2[i:i+len(ns)])):
      return False
  return True


r = []
for i in range(1, 1000000):
  if is_circular_prime(i):
    r.append(i)

print(r, len(r))




