def insert before(self,data):
    for i in data:
        node = Node(i)

        if self head next is None:
            self head next = node
        else:
            node next = self head next
            self head next = node