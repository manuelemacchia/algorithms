class Stack:
    def __init__(self, n):
        self.n = n  # maximum length of stack
        self.pos = -1  # current position inside stack (-1 is empty)
        self.stack = [None] * n
        
    def __repr__(self):
        return str(self.stack[:self.pos+1])
    
    def _stack_empty(self):
        if self.pos == -1:
            return True
        return False
    
    def push(self, elem):
        if self.pos == self.n-1:
            raise IndexError("Stack overflow")
        
        self.pos += 1
        self.stack[self.pos] = elem
    
    def pop(self):
        if self._stack_empty():
            raise IndexError("Stack underflow")
        
        self.pos -= 1
        return self.stack[self.pos+1]
    

# Example
my_stack = Stack(3)
print(my_stack)
my_stack.push(5)
my_stack.push(7)
my_stack.push(9)
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())