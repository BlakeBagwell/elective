class Node:
    def __init__(self, previous_node, next_node):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(self, new_node):
        if self.head is None && self.head is None:
            self.head = new_node,
            self.tail = new_node
        else:
            old_tail = self.tail_node
            self.tail_node = new_node
            new_node.previous_node = old_tail
            old_tail.next_node = new_node

    def dequeue(self):
        old_head = self.head
        self.head = old_head.next_node
        return old_head.value
