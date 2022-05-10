print(" 계산기 시작")

str1 = []
for i in range(7):
    str1 = [input("> ")]
    print(str1)
    if '' in str1:
        break

ans = 0
for x in range(len(str1)):
    if x == 0:
        if '.' in str1[x]:
            ans = float(str1[x])
        else:
            ans = int(str1[x])
    elif x % 2 == 0:
        if str[x-1] == '+':
            if '.' in str1[x]:
                ans += float(str[x])
            else:
                ans += int(str[x])
        elif str[x-1] == '-':
            if '.' in str1[x]:
                ans -= float(str[x])
            else:
                ans -= int(str[x])
        elif str[x-1] == '*':
            if '.' in str1[x]:
                ans *= float(str[x])
            else:
                ans *= int(str[x])
        elif str[x-1] == '/':
            if '.' in str1[x]:
                ans /= float(str[x])
            else:
                ans /= int(str[x])
if ans == int:
    print("계산 결과는 {}입니다.".format(ans))
elif ans == float:
    print("계산 결과는 {:.2f}입니다.".format(ans))
else:
    print(ans, type(ans))
