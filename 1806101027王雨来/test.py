stack = []

for i in 'hello,World!':
    stack.append(i)

result = []
while len(stack) != 0:
    result.append(stack.pop())
print("".join(result))

#  快捷键：Ctrl+w\x\d

aa=[1,2,3,4,5,6]
bb=aa.pop()
print(aa)

