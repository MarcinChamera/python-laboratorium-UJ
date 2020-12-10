class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(N)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.tail == self.head:
            self.head = self.tail = None
        else:
            current_node = self.head
            for _ in range(self.length - 1):
                current_node = current_node.next
                # if current_node.next == self.tail:
                #     current_node.next = None
                #     break
            current_node.next = None
        self.length -= 1
        return node

    def merge(self, other):   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        self.tail.next = other.head
        self.length += other.length
        other.clear()

    def clear(self):     # czyszczenie listy
        self.head = None
        self.length = 0

    def print(self):
        current = self.head
        if current is None:
            print("lista pusta")
        else:
            print("elementy listy:")
            for _ in range(self.length):
                print(current)
                current = current.next

if __name__ == '__main__':
    # Zastosowanie.
    alist = SingleList()
    alist.insert_head(Node(11))         
    alist.insert_head(Node(22))         
    alist.insert_tail(Node(33))
    alist.print()         
    blist = SingleList()
    blist.insert_head(Node(44))         
    blist.insert_head(Node(55))         
    blist.insert_tail(Node(66))
    blist.print()
    alist.merge(blist)
    alist.print()
    alist.remove_tail()
    alist.print()
    alist.clear()
    alist.print()
    