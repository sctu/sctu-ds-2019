# 编程实现括号匹配。

stack = []
LEFT = ['{', '[', '(']
RIGHT = ['}', ']', ')']

# 1. 针对每一个字符进行处理：
for i in '{[()]}':

# 2. 如果是左括号，则入栈。
    if i in LEFT:
        stack.append(i)

# 3. 如果是右括号，则进行匹配。
    if i in RIGHT:
        left = stack.pop()

# 4. 当所有的字符都处理完成后，
#    判断栈是否为空。

