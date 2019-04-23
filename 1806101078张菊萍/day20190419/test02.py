# 编程实现括号匹配
# {[()]}

str = '{[()]}'
stack = []
LEFT = '{[('
RIGHT = '}])'

# 1. 依次遍历字符串的每一个字符
for ch in str:
    print(ch)

# 2. 如果是当前字符左括号，入栈
    if ch is '(' or \
       ch is '[' or \
       ch is '{':
        stack.append(ch)

# 3. 如果是右括号，
#    出栈并且与当前左括号进行匹配。
#    如果不匹配，return False
#    如果匹配则继续。


# 4. 当所有字符都处理完成后，
#   栈不为空，返回False
#   如果栈为空，return True
