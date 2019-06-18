def __init__(self):
    self.stack=[]
    self.minStack=[]

def push(self,x):
    self.stack.append(x)
    if not self.minStack or self.minStack[-1]>=x:
        self.minStack.append(x)

def pop(self):
    if self minStack[-1]==self.stack[-1]:
        del self.minStack[-1]
    self.stack.pop()

def top(self):
    return self.stack[-1]

def getMin(self):
    return self.minStack[-1]