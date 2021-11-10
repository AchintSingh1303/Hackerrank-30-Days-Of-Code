def insert(self, head, data):
    if (head == None):
        head = Node(data)
    elif (head.next == None):
        head.next = Node(data)
    else:
        self.insert(head.next, data)
    return head