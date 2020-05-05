"""
세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때, p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까?
"""

def answer(k):
    def find(x):
        count = 0
        for a in range(1, (x // 3) + 1):
            for b in range(1, (x // 2)):
                c = x - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    count += 1

        return count

    result = 0
    max_val = 0
    for i in range(1, k + 1):
        val = find(i)
        if max_val < val:
            max_val = val
            result = i

    return result


# print(answer(1000))

################################################################
from time import time
from collections import Counter

t = time()

def divi3(num):
    result = []

    for a in range(1, int(num/3)):

        for b in range(a+1, int((num-a)/2)+1):
            c = a**2 + b**2
            if c**0.5 == int(c**0.5) and c**0.5 + a + b <= num:
                result.append(int(c**0.5 + a + b))

    return result

_answer = Counter(divi3(1001)).most_common(1)[0]


t1 = time() - t

# print(_answer, "---",str(t1)[0:5], "초")

################################################################


import time
tic = time.time()
def is_jikgak(a,b,c):
    return a**2+b**2 == c**2


def is_plus(a,b,c):
    return int(a)==a and int(b)==b and int(c)==c


tris = {}
for b in range(1,500):
    for a in range(1,b):
        c = (a**2 + b**2)**0.5
        if is_plus(a,b,c) and a+b+c<=1000:
            if is_jikgak(a,b,c):
                print(a,b,c, a+b+c)
                if a+b+c in tris:
                    tris[a+b+c] += 1
                else:
                    tris[a+b+c] = 1
        else: continue

mkey = 0
mval = 0
for key, val in tris.items():
    if mval < val:
        mval = val
        mkey = key

print(mkey, mval)
print(time.time()-tic, 'sec')
################################################################