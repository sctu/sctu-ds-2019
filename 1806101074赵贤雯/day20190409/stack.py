stack = []
'''
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(3)
stack.append(3)
stack.append(3)
'''

#ctrl+d（复制）
#ctrl+x（删除）
#ctrl+w（选中）

'''print(stack.pop())
print(stack.pop())
print(stack.pop())'''


#当栈不为空的时候一直pop
'''
while len(stack) is not 0:
    print(stack.pop())
    '''

for i in range(1,11):
    stack.append(i)
    print(stack)
