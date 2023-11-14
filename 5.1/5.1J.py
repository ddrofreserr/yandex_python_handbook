class Stack:

    def __init__(self):
        self.sequence = []

    def push(self, item):
        self.sequence += [item]

    def pop(self):
        if not self.is_empty():
            return self.sequence.pop()
    
    def is_empty(self):
        if len(self.sequence) == 0:
            return True
        else:
            return False
