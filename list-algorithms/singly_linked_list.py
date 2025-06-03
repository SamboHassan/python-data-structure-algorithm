class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insertFirst(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        self.count += 1

    def insertLast(self, data):
        node = Node(data)
        if self.head is None:
            # If the list is empty, insert at head
            self.head = node
        else:
            current = self.head
            # Traverse to the last node
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(node)

        self.count += 1

    def insertAt(self, position, data):
        if position < 1 or position > self.count + 1:
            raise IndexError("Invalid position")

        node = Node(data)
        # Insert at the head (position 1)
        if position == 1:
            node.set_next(self.head)
            self.head = node
        else:
            current = self.head
            count = 1

            while count < position - 1:
                current = current.get_next()
                count += 1

            node.set_next(current.get_next())
            current.set_next(node)

        self.count += 1

    def find(self, data):
        tempnode = self.head
        while tempnode != None:
            if tempnode.get_data() == data:
                return tempnode
            else:
                tempnode = tempnode.get_next()
        return None

        # WRONG

    # def deleteAt(self, idx):
    #     if idx > self.count:
    #         return
    #     if self.head == None:
    #         return
    #     else:
    #         node = self.head
    #         tempidx = 0
    #         while tempidx < idx - 1:
    #             node = node.get_next()
    #             tempidx += 1
    #         node.set_next(node.get_next().get_next())
    #         self.count -= 1

    def deleteAt(self, idx):
        if idx < 1 or idx > self.count:
            raise IndexError("Invalid index")
        if self.head is None:
            return

        if idx == 1:
            self.head = self.head.get_next()
        else:
            node = self.head
            tempidx = 1
            while tempidx < idx - 1:
                node = node.get_next()
                tempidx += 1
            node.set_next(node.get_next().get_next())

        self.count -= 1

    def delete2(self, position):
        # Check if the position is valid
        if position < 1 or position > self.count:
            raise IndexError("Invalid position")

        # If deleting the first node
        if position == 1:
            self.head = self.head.next
        else:
            previous = self.head
            count = 1

            # Traverse to the node just before the one to delete
            while count < position - 1:
                previous = previous.next
                count += 1

            current = previous.next
            previous.next = current.next

        self.count -= 1

    # def dump_list(self):
    #     if self.head == None:
    #         return
    #     tempnode = self.head
    #     while tempnode != None:
    #         print("Node: ", tempnode.get_data())
    #         tempnode = tempnode.get_next()

    # More pythonic version
    def dump_list(self):
        tempnode = self.head
        while tempnode:
            print("Node:", tempnode.get_data())
            tempnode = tempnode.get_next()


itemlist = LinkedList()

itemlist.insertLast(12)
itemlist.insertLast(13)
itemlist.insertLast(14)
itemlist.insertFirst(15)
itemlist.insertFirst(20)
itemlist.dump_list()

print("Before deletion", itemlist.get_count())
print(itemlist.find(14).get_data())

print()
print(itemlist.deleteAt(2))
itemlist.dump_list()
print("After deletion", itemlist.get_count())

# Help me debug this code
