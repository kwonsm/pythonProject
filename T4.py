"""
a = input("계산 식을 입력 하세요> ")

if '+' in a:
    num1 = a[:a.find('+')-1]
    num2 = a[a.find('+')+1:]
    print(num1, num2)
    if '.' in a:
        num1 = float(num1)
        num2 = float(num2)
        print("결과 {:.2f}입니다.".format(num1+num2))
    else:

        print("결과 {:d}입니다.".format(num1+num2))
elif '-' in a:
    num1 = a[:a.find('-') - 1]
    num2 = a[a.find('-') + 1:]
    if '.' in a:
        num1 = float(num1)
        num2 = float(num2)
        print("결과 {:.2f}입니다.".format(num1 - num2))
    else:

        print("결과 {:d}입니다.".format(num1 - num2))
elif '*' in a:
    num1 = a[:a.find('*') - 1]
    num2 = a[a.find('*') + 1:]
    if '.' in a:
        num1 = float(num1)
        num2 = float(num2)
        print("결과 {:.2f}입니다.".format(num1 * num2))
    else:

        print("결과 {:d}입니다.".format(num1 * num2))
elif '/' in a:
    num1 = a[:a.find('/') - 1]
    num2 = a[a.find('/') + 1:]
    if '.' in a:
        num1 = float(num1)
        num2 = float(num2)
        print("결과 {:.2f}입니다.".format(num1 / num2))
    else:

        print("결과 {:.2f}입니다.".format(num1 / num2))
"""


a = input("계산 식을 입력 하세요> ")

if '+' in a:
    num1 = a[:a.find('+')]
    num2 = a[a.find('+')+1:]
elif '-' in a:
    num1 = a[:a.find('-')]
    num2 = a[a.find('-') + 1:]
elif '/' in a:
    num1 = a[:a.find('/')]
    num2 = a[a.find('/') + 1:]
elif '*' in a:
    num1 = a[:a.find('/')]
    num2 = a[a.find('/') + 1:]

print(num1, num2)

if '.' in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

