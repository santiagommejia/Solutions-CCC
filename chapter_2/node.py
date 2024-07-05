class Node():
    data = None
    prev = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def append_node_to_tail(self, node):
        n = self
        while n.next != None:
            n = n.next
        n.next = node