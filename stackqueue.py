class Queue:
    def __init__(self):
        self.stack = []
    
    def push(self, item):

        self.stack.append(item)
        print(f"Pusholt: {item}")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            print("Stack üres. Nem lehet poppolni.")
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack üres. Nem lehet peekelni.")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


stack = Queue()
stack.push(10)
stack.push(0)
stack.push(120)
stack.push(71)
print("Poppolt:", stack.pop())
print("Legfelső elem:", stack.peek())
print("Stack mérete:", stack.size())
