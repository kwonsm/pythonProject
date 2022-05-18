class Stack:
    def __init__(self, c=5):
        self.capacity = c
        self. stack = []
        self.t = -1
        self.size = 0

    def top(self):
        return self.t

    def push(self, data):
        if self.size == self.capacity:
            print("스택이 가득 찼습니다.")
        else:
            self.stack.append(data)
            self.size += 1
            self.t = data
        print(self.stack)

    def pop(self):
        if self.size == 0:
            print("스택이 비어있습니다.")
        else:
            self.size -= 1
            del self.stack[-1]

            if self.size == 0:
                self.t = -1
            else:
                self.t = self.stack[-1]
        print(self.stack)

