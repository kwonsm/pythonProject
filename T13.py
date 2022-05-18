from data_structure import Stack_class

stackA = Stack_class.Stack(5)
while True:
    order = input("작업을 입력하세요. (종료: -1)\n(pop, push, top, print)\n")

    if order == "pop":
        stackA.pop()
    elif order == "push":
        data = input("데이터를 입력하세요> ")
        stackA.push(data)
    elif order == "top":
        print("{}".format(stackA.top()))
    elif order == "-1":
        break
