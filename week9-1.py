list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
list_num = False
list_error = False
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        print("오류가 발생했습니다 : ", item)
        list_num = False
        list_error = True
    else:
        print("오류가 발생하지않았습니다.")
    finally:
        print("프로그램을 종료합니다.")
print("{}내부에 있는 숫자는 \n{}입니다.".format(list_input_a, list_number))


