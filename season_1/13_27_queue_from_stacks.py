class MyQueue:

    frontface = None
    backface  = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.frontface = []
        self.backface  = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.frontface) > 0:
            self.backface.append(self.frontface.pop())
        
        self.backface.append(x)
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.backface) > 0:
            self.frontface.append(self.backface.pop())
        
        return self.frontface.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.backface) > 0:
            self.frontface.append(self.backface.pop())
        
        return self.frontface[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        if len(self.frontface) > 0 or len(self.backface) > 0:
            return False
        
        return True