import sys

#this is example of min heap 

#    i 
# (i-1) / 2

            #    5
            # /   \
        #   6      8
        #  /
        # 3  

class Heap:

    def __init__(self, heap_capacity):
        self.heap_capacity = heap_capacity
        self.heap_size = 0
        self.heap = [0]*heap_capacity

    def swap (self, i, j ):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return (2*i+1)
    
    def right(self, i):
        return (2*i+2)
     
    def insert(self, value):
        if self.heap_capacity == self.heap_size:
            print("heap overflow")
            return
        i = self.heap_size
        self.heap[i] = value
        self.heap_size+=1

        while (i !=0 and self.heap[i] < self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def deceaseMin(self, i, new_val):
        self.heap[i] = new_val
        while(i!=0 and self.heap[i] < self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)
        
    def extractMin(self):
        if (self.heap_size<=0):
            return sys.maxsize
        
        if (self.heap_size ==1 ):
            self.heap_size=0
            return self.heap[0]
        minvalue = self.heap [0]
        i = self.heap_size-1
        self.heap_size-=1
        self.heap[0] = self.heap[i]
        self.minheapify(0)
        return minvalue

        
    def printHeap(self):
        print(self.heap[:self.heap_size])


    def delete(self, i):
        self.deceaseMin(i, -1)
        self.extractMin()
        

    def minheapify(self, i):
        l = self.left(i)
        r = self.right(i)
        small = i
        if(l < self.heap_size and self.heap[l] < self.heap[i]):
            small = l
        if(r < self.heap_size and self.heap[r] < self.heap[small]):
            small = r
        if (small != i) : 
            self.swap(i, small)
            self.minheapify(small)
    
    
heap = Heap(10)
heap.printHeap()
heap.insert(34) 
heap.printHeap()
heap.insert(13)
heap.insert(54)
heap.insert(35)
heap.printHeap()
heap.insert(4)
heap.printHeap()
heap.delete(3)
print("hepi")
heap.printHeap()
heap.delete(3)
heap.delete(3)
heap.printHeap()