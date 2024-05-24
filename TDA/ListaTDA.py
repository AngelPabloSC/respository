import random
from abc import ABC, abstractmethod

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListaTDA(ABC):
    @abstractmethod
    def insertar(self, value):
        pass

    @abstractmethod
    def eliminar_ultimo_insertado(self):
        pass

class LinkedList(ListaTDA):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  
        self.size += 1

    def eliminar_ultimo_insertado(self):
        if not self.head:
            print("La lista está vacía.")
            return

        current = self.head
        prev = None

        while current.next:
            prev = current
            current = current.next

        if prev:
            prev.next = None
        else:
            self.head = None

        self.size -= 1
        print("Elemento eliminado:", current.value)

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Ejemplo de uso
if __name__ == "__main__":
    linked_list = LinkedList()

    for _ in range(10):
        random_num = random.randint(1, 100)
        linked_list.insertar(random_num)

    linked_list.display()

    linked_list.eliminar_ultimo_insertado()
    linked_list.display()
    
    print("Tamaño del array:", linked_list.size)
