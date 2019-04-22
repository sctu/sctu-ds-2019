#2、编程实现括号匹配。
#
#输入：{[()]}
#
#输出：True

# {[()]}

str = '{[()]}'
stack = []
LEFT = '{[('
RIGHT = '}])'

# 1. 依次遍历每一个字符
for ch in str:
    print(ch)

# 2. 如果是左括号，入栈
    if ch is '(' or \
       ch is '[' or \
       ch is '{':
        stack.append(ch)