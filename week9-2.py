while True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = a/b
        print("{}/{}={}".format(a, b, c))
    except ValueError:
        print("정수나 실수를 입력하세요")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print("미리 파악한 예외가 아닙니다.")
        print(type(e), e)
    else:
        break


num = input("정수 입력 >")
num = int(num)

if num > 0:
    raise NotImplementedError
else:
    raise NotImplementedError