class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            self.tail = node

    def find_node_at(self, index):
        if index == 0:
            return self.head
        else:
            node = self.head
            i = 0
            while i != index:
                node = node.next
                i += 1
            return node






