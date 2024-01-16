class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int):
        cur = self.head
        if cur is None or index < 0:
            return -1
        for i in range(index):
            cur = cur.next
            if cur is None:
                return -1
        return cur.val

    def addAtHead(self, val: int):
        self.head = Node(val, self.head)

    def addAtTail(self, val: int):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        node = Node(val)
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def addAtIndex(self, index: int, val: int):
        if self.head is None:
            if index == 0:
                self.addAtHead(val)
            else:
                return
        else:
            if index == 0:
                self.addAtHead(val)
            else:
                cur = self.head
                node = Node(val)

                for i in range(index-1):
                    cur = cur.next
                    if cur is None:
                        return
                node.next = cur.next
                cur.next = node

    def deleteAtIndex(self, index: int):
        if index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head

            for i in range(index - 1):
                cur = cur.next
                if cur is None:
                    return
            if cur.next is None:
                return
            cur.next = cur.next.next


    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.val, '>', cur.next)
            cur = cur.next
