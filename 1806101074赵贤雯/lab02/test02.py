# {[()]}
# 编程实现括号匹配


str = '{[()]}'
stack=[]
left=['{','[','(']
right=['}',']',')']
#1.依次遍历每一个字符
for ch in str:
    print(ch)

#2.如果是左括号，入栈
if ch in left:
    stack.append(ch)
#3.如果是右括号，
#  出栈并且与当前左括号进行匹配
#  如果不匹配，return False
#  如果匹配则继续
    if ch in right:
        left = stack.pop()

        if left.index(left) != right.index(ch):
            print("不匹配")

#4.当所有字符都处理完成后，
#  栈不为空，返回False
#  如果栈为空，return true
if len(stack) == 0:
    print("匹配")
else:
    print("不匹配")
