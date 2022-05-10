print("나눗셈 예외처리 a / b")
division = False

while not division:
    try:
        a = float(input("피제수(a) 입력> "))
        try:
            b = float(input("제수(b) 입력> "))
            try:
                a/b
            except:
                print("0으로 나눌 수 없습니다.")
            else:
                division = True
        except:
            print("정수 또는 실수만 입력하세요.")
    except:
        print("정수 또는 실수만 입력하세요.")


print("{} / {} = {}".format(a, b, a/b))
