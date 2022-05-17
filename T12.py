from data_structure import *

stackA = []

while True:
    order = input("작업을 입력하세요. (pop, push, top, print)\n")
    if order == "push":
        stackA = stack.push(stackA, input("데이터를 입력하세요"))
    elif order == "pop":
        stackA = stack.pop(stackA)
    elif order == "top":
        stackA = stack.top(stackA)
    elif order == "print":
        stack.printStatck(stackA)
    elif order == "-1":
        break
