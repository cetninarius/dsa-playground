class MyCircularQueue:

    def __init__(self, k: int):
        self.data = self.set_size(k)
        self.head = -1
        self.tail = -1
        self.size = k

    def set_size(self, k):
        d = {}
        for i in range(k):
            d[i] = 0
        return d

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.data[0] = value
            return True
        if not self.isFull():
            self.tail = (self.tail + 1) % self.size
            self.data[self.tail] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.data[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.data[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        sub = self.tail - self.head
        if sub == self.size - 1 or sub == -1:
            return True
        else:
            return False

    def printList(self):
        print(f'Head: {self.head}, Tail: {self.tail}')
        print(self.data.values())
