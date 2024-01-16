from linked_list import MyLinkedList

lista = MyLinkedList()
lista.addAtHead(5)
lista.addAtHead(10)
lista.addAtTail(15)
lista.addAtIndex(0, 2)
print(lista.get(2))
lista.deleteAtIndex(6)
lista.printList()

