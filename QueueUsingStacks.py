class MyStack:

    def __init__(self):
        self.data = list()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if len(self.data) == 0:
            return None
        val = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        return val

    def top(self) -> int:
        if len(self.data) == 0:
            return None
        return self.data[len(self.data)-1]

    def empty(self) -> bool:
        return self.top() is None

    def size(self) -> int:
        return len(self.data)


class MyQueue:

    def __init__(self):
        self.stack = MyStack()

    def push(self, x: int) -> None:
        """ enqueue """
        self.stack.push(x)

    def pop(self) -> int:
        """ dequeue """
        if self.stack.empty():
            return None
        temp_stack = MyStack()
        top = self.stack.pop()
        while not self.stack.empty():
            temp_stack.push(top)
            top = self.stack.pop()
        while not temp_stack.empty():
            self.stack.push(temp_stack.pop())
        return top

    def peek(self) -> int:
        return self.stack.data[0]

    def empty(self) -> bool:
        return self.stack.empty()


obj = MyQueue()
# obj.push(2)
# print(obj.pop())
# print(obj.peek())
# print(obj.empty())
#
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())

print(obj.pop())
print(obj.pop())
print(obj.pop())
