from linked_list import MyLinkedList

lista = MyLinkedList()
lista.addAtHead(1)
lista.addAtTail(2)
lista.addAtTail(3)
lista.addAtTail(3)
lista.addAtTail(2)
lista.addAtTail(1)

print(lista.isPalindrome())

lista.printList()




