class MyCircularQueue:

    queue = None
    first = 0
    last = 0
    size = None

    def __init__(self, k: int):
        prev = None 

        self.queue = [None for _ in range(k)]
        self.size = k
        return 
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        if not self.isFull():

            if not self.isEmpty():
                self.last += 1
                self.last %= self.size
            
            self.queue[self.last] = value
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue[self.first] = None

            if self.first != self.last:
                self.first += 1
                self.first %= self.size
                
            return True
        else:
            return False
        return

        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.queue[self.first]
        else:
            return -1
        return
        
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.queue[self.last]
        else:
            return -1
        return

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.queue[self.first] is None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        next = self.last + 1
        next %= self.size
        if next == self.first and self.queue[self.first] is not None:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()