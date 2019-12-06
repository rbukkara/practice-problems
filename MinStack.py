class Node:
    def __init__(self, value: int):
        self.val = value
        self.mini = value

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()

    def push(self, x: int) -> None:

        node = Node(x)
        if len(self.data) > 0:
            cur_top = self.data[len(self.data)-1]
            if cur_top.mini < x:
                node.mini = cur_top.mini
        self.data.append(node)

    def pop(self) -> None:
        del self.data[len(self.data)-1]

    def top(self) -> int:
        return self.data[len(self.data)-1].val

    def getMin(self) -> int:
        return self.data[len(self.data)-1].mini


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(15)
print(obj.top())
print(obj.getMin())

obj.push(4)
print(obj.top())
print(obj.getMin())

obj.pop()
print(obj.top())
print(obj.getMin())