class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data, priority):
        node = Node(data, priority)
        if (self.isEmpty()):
            self.head = node
        else:
            if (self.head.priority < priority):
                node.next = self.head
                self.head = node
            else:
                current = self.head
                while (current.next and current.next.priority > priority):
                     current = current.next
                tmp = current.next
                current.next = node
                node.next = tmp 

    def pop(self):
        tmp = self.head
        self.head = self.head.next
        return tmp.data , tmp. priority

    def peek(self):
        return self.head.data, self.head. priority


pq = PriorityQueue()
pq.add(34, 4)
pq.add(13, 43)
pq.add(324, 44)
pq.add(3, 0)
pq.add(23, 42)

print(pq.peek())
pq.pop()
print(pq.peek())
pq.pop()

print(pq.peek())
