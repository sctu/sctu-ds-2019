str = input('请输入：')
stack = []

for i in str:
    stack.append(i)
while len(stack) is not 0:
    stack.pop()
a = ''.join(stack)
if a==stack:
    print('ture')
else:
    print('flase')