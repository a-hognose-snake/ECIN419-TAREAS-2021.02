# Lista Doblemente Enlazada

# Clase Nodo
class DoublyLinkedListItem:
    def __init__(self, value):
        self.value = value
        self.nextItem = None
        self.previousItem = None
        self.list = None

    def GetList(self):
        return self.list

    def GetNext(self):
        return self.nextItem

    def GetPrevious(self):
        return self.previousItem

# Clase Lista
class DoublyLinkedList:
    def __init__(self):
        self.firstItem = None
        self.lastItem = None

    # Add First
    def addFirst(self, item):
        newItem = DoublyLinkedListItem(item)
        if self.firstItem is None:
            self.firstItem = newItem
            self.lastItem = newItem
            newItem.list = self
        else:
            self.firstItem.nextItem = newItem
            newItem.previousItem = self.firstItem
            self.firstItem = newItem

    # toString
    def toString(self):
        text = ""
        current = self.firstItem
        while current is not None:
            if current.previousItem is None:
                text += f"{current.value}"
            else:
                text += f"{current.value}, "
            current = current.previousItem
        return text

    # Add Last
    def addLast(self, item):
        newItem = DoublyLinkedListItem(item)
        if self.firstItem is None:
            self.firstItem = newItem
            self.lastItem = newItem
            newItem.list = self
        else:
            self.lastItem.previousItem = newItem
            newItem.nextItem = self.lastItem
            self.lastItem = newItem

    # Find Node
    def findNode(self, item):
        current = self.firstItem
        while current is not None:
            if current.value is item:
                return current
            current = current.previousItem

    # Add After
    def addAfter(self, item, afterItem):
        reference = self.findNode(afterItem)
        if reference is None:
            print("\nNo existe el nodo de referencia.\n")
        else:
            newItem = DoublyLinkedListItem(item)
            if reference is self.lastItem:
                reference.previousItem = newItem
                newItem.nextItem = reference
                self.lastItem = newItem
            else:
                reference.previousItem.nextItem = newItem
                newItem.previousItem = reference.previousItem
                reference.previousItem = newItem
                newItem.nextItem = reference

    # Add Before
    def addBefore(self, item, beforeItem):
        reference = self.findNode(beforeItem)
        if reference is None:
            print("\nNo existe el nodo de referencia.\n")
        else:
            newItem = DoublyLinkedListItem(item)
            if reference is self.firstItem:
                reference.nextItem = newItem
                newItem.previousItem = reference
                self.firstItem = newItem
            else:
                reference.nextItem.previousItem = newItem
                newItem.nextItem = reference.nextItem
                newItem.previousItem = reference
                reference.nextItem = newItem

    # Clear: Se borran todas las referencias
    def clear(self):
        self.firstItem = None
        self.lastItem = None
        print("Todo ha sido borrado.\n")

    # Contains
    def contains(self, item):
        current = self.firstItem
        while current is not None:
            if current.value is item:
                print(f"La lista contiene {item}.\n")
                return True
            current = current.previousItem

    # Remove
    def remove(self,item):
        n = self.findNode(item)
        if n is None:
            print("\nNo existe el nodo a eliminar.\n")
        else:
            if n is self.firstItem:
                self.removeFirst()
            else:
                if n is self.lastItem:
                    self.removeLast()
                else:
                    n.nextItem.previousItem = n.previousItem
                    n.previousItem.nextItem = n.nextItem
                    n.nextItem = None
                    n.prevItem = None


    # RemoveFirst
    def removeFirst(self):
        current = self.firstItem
        if current.nextItem is None and current.previousItem is None:
            self.firstItem = None
            self.lastItem = None
            print("\nSe elimino el primero. No hay mas nodos.\n")
        else:
            current.previousItem.nextItem = None
            self.firstItem = current.previousItem
            print("\nSe elimino el primero.\n")

    # RemoveLast
    def removeLast(self):
        current = self.lastItem
        if current.nextItem is None and current.previousItem is None:
            self.firstItem = None
            self.lastItem = None
            print("\nSe elimino el ultimo. No hay mas nodos.\n")
        else:
            current.nextItem.previousItem = None
            self.lastItem = current.nextItem
            print("\nSe elimino el ultimo.\n")

# Test
List = DoublyLinkedList()
List.addLast(5)
List.addLast(6)
List.addLast(7)
List.addLast(8)
print(List.toString())
List.removeFirst()
print(List.toString())
List.addAfter(10, 8)
print(List.toString())
List.addBefore(20, 8)
print(List.toString())
List.remove(10)
print(List.toString())
List.remove(8)
print(List.toString())