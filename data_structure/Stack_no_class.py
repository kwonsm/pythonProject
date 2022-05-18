stack_capacity = 5


def top(lista=[]):
    if len(lista) == 0:
        print("빈 리스트입니다.")
    else:
        print("top:", lista[len(lista)-1])


def push(data, lista=[]):
    if len(lista) == stack_capacity:
        print("스택이 가득 찼습니다.")
        return lista
    else:
        lista.append(data)
        return lista


def pop(lista=[]):
    if len(lista) == 0:
        print("빈 스택입니다.")
        return lista
    else:
        data = lista[len(lista)-1]
        print("제거한 요소:", data)
        del lista[len(lista)-1]
        return lista


def printStack(lista=[]):
    print(lista)
    if len(lista) == 0:
        print("스택이 비어있습니다.")


if __name__ == "__main__":
    test = [1, 2, 1, 1, 1]
    printStack(test)