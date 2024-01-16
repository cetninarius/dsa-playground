from typing import Optional


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> Optional[Node]:
        """
        Gets the Node object at the given index
        :param index:
        :return Optional[Node]:
        """
        cur = self.head
        if cur is None or index < 0:
            return None
        for i in range(index):
            cur = cur.next
            if cur is None:
                return None
        return cur

    def get_index(self, node: Node) -> int:
        """
        Gets index of a Node object if it's found in the list, otherwise -1
        :param node:
        :return int:
        """
        cur = self.head
        indx = 0
        if not self.hasCycle():
            while cur:
                if cur == node:
                    return indx
                indx += 1
                cur = cur.next
        else:
            loop = False
            intersect = self.detectCycle()
            while cur:
                if cur == node:
                    return indx
                if cur == intersect:
                    if not loop:
                        loop = True
                    else:
                        break
                indx += 1
                cur = cur.next


    def addAtHead(self, val: int):
        """
        Adds a value at the head of the list
        :param val:
        :return:
        """
        self.head = Node(val, self.head)

    def addAtTail(self, val: int):
        """
        Adds a value at the tail of the list
        :param val:
        :return:
        """
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        node = Node(val)
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def addAtIndex(self, index: int, val: int):
        """
        Adds a value at a specified index
        :param index:
        :param val:
        :return:
        """
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
        """
        Deletes a Node at a specified index
        :param index:
        :return:
        """
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

    def hasCycle(self) -> bool:
        """
        Returns True if the list has a Cycle, otherwise False
        :return bool:
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def detectCycle(self) -> Optional[Node]:
        """
        Returns the Node that represents start of the cycle
        :return Optional[Node]:
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def removeNthFromEnd(self, n: int):
        """
        Removes nth element from the end of the list
        :param n:
        :retur:
        """
        right = self.head
        left = self.head
        for i in range(n):
            if right is None:
                return
            right = right.next
        if right is None:
            self.head = self.head.next
            return
        right = right.next
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

    def reverseList(self):
        """
        Reverses the list order
        :return:
        """
        prev = None
        cur = self.head
        while cur:
            tmp = cur.next
            cur = Node(cur.val)
            cur.next = prev
            prev = cur
            cur = tmp
        self.head = prev

    def delete(self, val: int) -> bool:
        """
        Deletes the first occurrence of a value. Returns True if value found, otherwise False
        :param val:
        :return bool:
        """
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def deleteAll(self, val: int):
        """
        Deletes all occurrences of a value
        :param val:
        :return:
        """
        cur = self.head

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        while self.head and self.head.val == val:
            self.head = self.head.next

    def length(self) -> int:
        """
        Returns the length of the list
        :return int:
        """
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def oddEvenList(self):
        """
        Groups elements with odd and even indexes (e.g. 12345 -> 13524)
        :return:
        """
        if not self.head or not self.head.next or not self.head.next.next:
            return
        odd = self.head
        even = odd.next
        cur = even.next
        while cur:
            nxt = cur.next

            cur.next = odd.next
            odd.next = cur
            odd = odd.next
            even.next = nxt
            even = even.next
            if nxt:
                cur = nxt.next
            else:
                return

    def isPalindrome(self) -> bool:
        cur = self.head
        stack = []
        palin = False
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = self.head
        while cur:
            i = stack.pop()
            if cur.val == i:
                palin = True
            else:
                palin = False
                return palin
            cur = cur.next

        return palin


    def printList(self) -> int:
        """
        Prints the list, connection by connection. Returns -1 if the list has a Cycle
        :return int:
        """
        if self.hasCycle():
            return -1
        cur = self.head
        while cur is not None:
            print(cur.val, '>', cur.next)
            cur = cur.next
        return 1
