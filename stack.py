class Stack:
    def __init__(self): self.items = []
    
    def is_empty(self): return not self.items
    def push(self, item): self.items.append(item)

def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def size(self): return len(self.items)
    def display(self): return self.items

# Dynamic input for stack operations
s = Stack()
print(s.is_empty())
for item in input("Enter elements to push (comma-separated): ").split(','):
    s.push(item.strip())
print("Size:", s.size())
print("Stack:", s.display())
print("Peek:", s.peek())

# Pop operations
print("Popped:", s.pop())
print("Stack after pop:", s.display())
print("Size:", s.size())
