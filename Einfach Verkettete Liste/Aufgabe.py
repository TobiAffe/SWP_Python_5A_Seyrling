import random

class Node:
    def __init__(self, value):
        """
        Knoten einer einfach verketteten Liste.
        Enthält einen Wert und einen Verweis auf das nächste Element.
        """
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        """
        Implementierung einer einfach verketteten Liste.
        """
        self.head = None  # Startknoten der Liste
        self.length = 0  # Anzahl der Elemente in der Liste

    def append(self, value):
        """
        Fügt ein neues Element am Ende der Liste hinzu.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def __len__(self):
        """
        Gibt die Länge der Liste zurück.
        """
        return self.length

    def __iter__(self):
        """
        Initialisiert den Iterator für die Liste.
        Setzt den Startpunkt für die Iteration.
        """
        self._iter_node = self.head  # Start der Iteration beim Kopf der Liste
        return self

    def __next__(self):
        """
        Gibt das nächste Element der Liste zurück.
        Falls keine weiteren Elemente vorhanden sind, wird eine StopIteration ausgelöst.
        """
        if self._iter_node is None:
            raise StopIteration  # Beendet die Iteration, wenn das Ende der Liste erreicht ist
        value = self._iter_node.value  # Speichert den aktuellen Wert
        self._iter_node = self._iter_node.next  # Bewegt den Zeiger auf das nächste Element
        return value

    def __str__(self):
        """
        Gibt eine lesbare Darstellung der Liste zurück.
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)

if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(10):  # 10 zufällige Zahlen einfügen
        linked_list.append(random.randint(1, 100))

    print("Verkettete Liste:")
    print(linked_list)
    print("Länge der Liste:", len(linked_list))
    print("Alle Elemente iterieren:")
    for value in linked_list:
        print(value)
