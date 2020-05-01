"""
1부터 5까지의 숫자를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
  115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.
"""

def answer(n):
    Ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    Eles = ['eleven', 'twelve',  'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen']
    Tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hund = 'hundred'
    thou = 'thousand'


    result = 0
    for i in range(1, n + 1):
        if i <= 10:
            result += len(Ones[i - 1])

        elif i < 100:
            if i < 20:
                result += len(Eles[i - 11])
            else:
                string = str(i)
                if string[1] == '0':
                    result += len(Tens[int(string[0]) - 2])
                else:
                    result += len(Tens[(i // 10) - 2]) + len(Ones[int(string[1]) - 1])

        elif i < 1000:
            first = Ones[(i // 100) - 1] + hund
            second = ''
            third = ''
            val = i % 100
            if val == 0:
                result = result + len(first)
            else:
                if val <= 10:
                    third = Ones[val - 1]
                else:
                    if val < 20:
                        second = Eles[val - 11]
                    else:
                        string = str(val)
                        if string[1] == '0':
                            second = Tens[int(string[0]) - 2]
                        else:
                            second = Tens[val // 10 - 2]
                            third = Ones[int(string[1]) - 1]

                result = result + len(first + second + third) + len('and')
        else:
            result = result + len(thou) + len(Ones[0])
    return result

print(answer(1000))