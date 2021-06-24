class Queue:
    def __init__(self, n):
        self.n = n
        self.head = 0
        self.tail = 0
        self.queue = [None] * (n+1)  # See note 1
        
    def __repr__(self):
        return (
            f"{str(self.queue)}\n"
            f"head: {self.head}, tail: {self.tail}"
        )
        
    def enqueue(self, elem):
        if self.tail+1 == self.head:
            raise IndexError("Queue is full")
        
        self.queue[self.tail] = elem
        
        if self.tail == self.n:
            self.tail = 0  # wrap around
        else:
            self.tail += 1
    
    def dequeue(self):
        if self.head == self.tail:
            raise IndexError("Queue is empty")
        
        dequeued = self.queue[self.head]
        
        if self.head == self.n:
            self.head = 0  # wrap around
        else:
            self.head += 1
        
        return dequeued
    

# Note 1
# In circular buffers, such as the one implemented by the queue, there is no
# clean way to differentiate the case where the buffer (queue) is full and where
# it is empty. In both cases, we'd have self.head==self.tail.
# To work around this problem:
# (1) use an array of N+1 elements to store a N-elements queue
# (2) when self.head==self.tail, the queue is empty
# (3) when self.head==(self.tail)
# Thus, an element of the array is reserved for checking if the queue is full.
# https://stackoverflow.com/a/56334755
    
    
# Example
queue = Queue(3)
print(queue)  # [x, x, x, x] h=0, t=0 -- queue empty (head==tail)

queue.enqueue(1)
print(queue)  # [1, x, x, x] h=0, t=1

queue.enqueue(2)
print(queue)  # [1, 2, x, x] h=0, t=2

print(queue.dequeue())  # -> 1
print(queue)  # [x, 2, x, x] h=1, t=2

queue.enqueue(3)
print(queue)  # [x, 2, 3, x] h=1, t=3

queue.enqueue(4)
print(queue)  # [x, 2, 3, 4] h=1, t=0

print(queue.dequeue())  # -> 2
print(queue)  # [x, x, 3, 4] h=2, t=0

queue.enqueue(5)
print(queue)  # [5, x, 3, 4] h=2, t=1 -- queue full (tail+1==head)

queue.enqueue(6)  # raises error
