class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return "<Node data: %s>" % self.data


class doublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        new_node = Node(data, next_node=self.head)
        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next_node:
                last = last.next_node
            last.next_node = new_node
            new_node.prev_node = last

    def insert(self, data, index=-1):
        if index >= self.size() or index == -1:
            self.append(data)
        elif index == 0:
            self.push(data)
        else:
            new_node = Node(data)
            last = self.head
            for i in range(index - 1):
                last = last.next_node
            new_node.next_node = last.next_node
            new_node.prev_node = last
            last.next_node = new_node
            nextnde = new_node.next_node
            nextnde.prev_node = new_node

    # ----------------------------------- TODO ----------------------------------- #

    def remove(self, key):
        temp = self.head
        prev = None
        if temp is not None:
            if temp.data == key:
                self.head = temp.next_node
                temp = None
                return 0
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next_node
        if temp == None:
            print(f'Key "{key}" was not found')
            return 1
        prev.next_node = temp.next_node
        temp = None
        return 0

    def deleteNode(self, node: Node):
        self.remove(node.data)
        # temp = self.head
        # prev = None
        # if temp is not None:
        #     if temp is node:
        #         self.head = temp.next_node
        #         temp = None
        #         return 0
        # while temp is not None:
        #     if temp is node:
        #         break
        #     prev = temp
        #     temp = temp.next_node
        # if temp == None:
        #     print(f'This Node "{node}" is not a part of this linked list')
        #     return 1
        # prev.next_node = temp.next_node
        # temp = None
        # return 0

    def pop(self, index=-1):
        if self.head == None:
            print("List is empty")
            return 1

        if index >= self.size() or index == -1:
            index = self.size() - 1

        last = self.head
        if index == 0:
            self.head = last.next_node
            return last.data
        else:
            prev = None
            for i in range(index):
                prev = last
                last = last.next_node
            prev.next_node = last.next_node
            return last.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return " <-> ".join(nodes)


if __name__ == "__main__":
    x = doublyLinkedList()
    x.push(0)
    x.push(1)
    x.push(3)
    x.push(4)
    x.insert(2, 2)
    x.insert("ALI", 2)
    print(x)
