stack=[]

stack.append('}')
stack.append(']')
stack.append('}')
stack.append(')')
stack.append('(')
stack.append('[')
stack.append('{')

while len(stack) !=0:
    print(stack.pop())

