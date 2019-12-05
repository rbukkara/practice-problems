# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        out = list()
        out.append(self.val)
        node = self.next
        while node:
            out.append(node.val)
            node = node.next
        return out


class LinkedList:

    def __init__(self):
        self.head = None

    def appendToTail(self, value):

        pointer = self.head
        if pointer is None:
            self.head = ListNode(value)
            return

        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = ListNode(value)

    def deleteAtTail(self) -> ListNode:

        pointer = self.head
        if pointer is None:
            return None

        while pointer is not None:
            if pointer.next is None:
                return pointer
            elif pointer.next.next is None:
                pointer.next = None
                return pointer.next
            pointer = pointer.next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = self.convertListToNumber(l1)
        num2 = self.convertListToNumber(l2)
        result = num1 + num2
        return self.convertNumberToList(result)

    def convertListToNumber(self, plist: ListNode) -> int:

        result = 0
        ind = 0
        while plist is not None:
            result = result + (10**ind) * plist.val
            plist = plist.next
            ind += 1
        return result

    def convertNumberToList(self, num: int) -> ListNode:

        lList = LinkedList()
        if num == 0:
            lList.appendToTail(0)
        else:
            while num > 0:
                lList.appendToTail(num % 10)
                num = num//10

        return lList.head

    def testAddNumbers(self,  l1: list(), l2: list(), res: list()):
        ll1 = LinkedList()
        for i in l1:
            ll1.appendToTail(i)

        ll2 = LinkedList()
        for i2 in l2:
            ll2.appendToTail(i2)

        actual = self.addTwoNumbers(ll1.head, ll2.head)
        act = actual.to_list()

        if act == res:
            print("pass")
        else:
            print("expected {0}. got {1}".format(res, act))


# sol = Solution()
# sol.testAddNumbers([2, 4, 3], [5, 6, 4], [7, 0, 8])
# sol.testAddNumbers([2, 0, 3], [5, 9, 2], [7, 9, 5])
# sol.testAddNumbers([1, 4, 5], [8, 2, 3], [9, 6, 8])
# sol.testAddNumbers([1, 1, 2], [1, 1, 2], [2, 2, 4])
# sol.testAddNumbers([0, 1, 2], [0, 0, 9], [0, 1, 1, 1])
# sol.testAddNumbers([1, 9, 9], [9, 0, 9], [0, 0, 9, 1])
# sol.testAddNumbers([8, 0, 0], [5, 6, 4], [3, 7, 4])
# sol.testAddNumbers([0], [0], [0])
# sol.testAddNumbers([0], [4], [4])
