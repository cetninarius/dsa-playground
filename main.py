from linked_list import MyLinkedList
from doubly_linked_list import MyDoublyLinkedList
from circular_queue import MyCircularQueue

lista = MyCircularQueue(3)

lista.printList()
print(lista.enQueue(1))
print(lista.enQueue(2))
print(lista.enQueue(3))
print(lista.enQueue(4))
print(lista.Rear())
print(lista.isFull())
print(lista.deQueue())
print(lista.enQueue(4))
print(lista.Rear())

lista.printList()




