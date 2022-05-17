from data_structure import *

stackA = []

while True:
    order = input("작업을 입력하세요. (pop, push, top, print)\n")
    if order == "push" or order == "push ":
        stackA = stack.push(input("데이터를 입력하세요> "), stackA)
    elif order == "pop" or order == "pop ":
        stackA = stack.pop(stackA)
    elif order == "top" or order == "top ":
        stackA = stack.top(stackA)
    elif order == "print" or order == "print ":
        stack.printStack(stackA)
    elif order == "-1" or order == "-1 ":
        break
