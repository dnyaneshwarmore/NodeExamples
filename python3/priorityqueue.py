class PriorityQueue:

    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def add(self, val):
        self.queue.append(val)
    
    def pop(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item

