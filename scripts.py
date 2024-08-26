class Node(object):
    def __init__(self, data):
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

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        self.count += 1

    def find(self, data):
        tempnode = self.head
        while tempnode != None:
            if tempnode.get_data() == data:
                return tempnode
            else:
                tempnode = tempnode.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            node = self.head
            tempidx = 0
            while tempidx < idx - 1:
                node = node.get_next()
                tempidx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        if self.head == None:
            return
        tempnode = self.head
        while tempnode != None:
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


itemlist = LinkedList()

itemlist.insert(12)
itemlist.insert(13)
itemlist.insert(14)
itemlist.insert(15)
itemlist.insert(20)
itemlist.dump_list()

print("Before deletion", itemlist.get_count())
print(itemlist.find(14).get_data())

print()
print(itemlist.deleteAt(2))
itemlist.dump_list()
print("After deletion", itemlist.get_count())
