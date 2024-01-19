class DNode:
    def __init__(self, val=None, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev


class MyDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1
        if index == 0:
            return self.head.val
        cur = self.head
        for i in range(index):
            if not cur or not cur.next:
                return -1
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = DNode(val)
        cur = self.head
        if cur:
            node.next = cur
            cur.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = DNode(val)
        cur = self.tail
        if cur:
            node.prev = cur
            cur.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        if index<0 or not self.head:
            return
        node = DNode(val)
        cur = self.head
        for i in range(index-1):
            if not cur or not cur.next:
                return
            cur = cur.next

        if not cur.next:
            self.addAtTail(val)
            return
        left = cur
        right = cur.next
        left.next = node
        node.next = right
        right.prev = node
        node.prev = left

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for i in range(index):
            if not cur or not cur.next:
                return
            cur = cur.next
        left = cur.prev
        right = cur.next
        if not right:
            left.next = None
            self.tail = left
            return
        left.next = right
        right.prev = left


    def printList(self) -> int:
        cur = self.head
        while cur is not None:
            print(cur.val, '>', cur.next)
            cur = cur.next
        return 1
