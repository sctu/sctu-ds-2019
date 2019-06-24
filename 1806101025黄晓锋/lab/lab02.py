'''实验二 栈和队列的应用
准备工作
栈的基本操作
新建python文件，命名为stack.py，输入下列内容开始练习。'''

stack = []

# 压栈
stack.append(1)
stack.append(2)
stack.append(3)

# 出栈
print(stack.pop())  # 输出：3
print(stack.pop())  # 输出：2
print(stack.pop())  # 输出：1

for i in range(1, 10):
    stack.append(i)

# 当栈不为空时
while len(stack) is not 0:
    print(stack.pop())
'''队列的基本操作
新建python文件，命名queue.py，输入下列内容开始练习。
'''
queue = []

# 入队
queue.append(1)
queue.append(2)
queue.append(3)

# 出队
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
'''1、编程实现字符串反转。

输入：Hello,World!

输出：!dlroW,olleH'''

def reverse_str(input_str):
    stack = []
    target = []

    for ch in input_str:
        stack.append(ch)

    while len(stack) != 0:
        ch = stack.pop()
        target.append(ch)

    return target


if __name__ == '__main__':
    reverse_str('Hello,World!')
'''2、编程实现括号匹配。

输入：{[()]}

输出：True'''

LEFT = ['(', '[', '{']
RIGHT = [')', ']', '}']


def parentheses_match(input_str):
    stack = []

    for ch in input_str:
        if ch in LEFT:
            stack.append(ch)
        elif ch in RIGHT:

            if len(stack) > 0 and RIGHT.index(ch) == LEFT.index(stack.pop()):
                continue
            else:
                return False

        else:
            print('The string contains not only parentheses!')
            return False

    if len(stack) == 0:
        return True

    return False


if __name__ == '__main__':
    print(parentheses_match('{[()]}'))
'''3、编程实现回文数判断。

输入：abcdcba

输出：True'''

def is_palindrome(input_str):
    str_len = len(input_str)
    stack = input_str[:str_len / 2]

    if str_len % 2 == 0:
        queue = input_str[str_len / 2:]
    else:
        queue = input_str[str_len / 2 + 1:]

    while len(stack) != 0 and len(queue) != 0:
        if stack.pop() == queue.pop(0):
            continue
        return False

    if len(stack) == 0 and len(queue) == 0:
        return True

    return False


if __name__ == '__main__':
    # 需要将字符串转化为list，然后再进行处理，否则会出错
    print(is_palindrome(list('abcdcba')))
'''4、编程实现MinStack.
'''
class MinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []

    def get_min(self):
        return self.min_stack[len(self.min_stack) - 1]

    def push(self, num):
        self.data.append(num)

        if len(self.min_stack) == 0:
            self.min_stack.append(num)
        elif self.get_min() > num:
            self.min_stack.append(num)
        else:
            self.min_stack.append(self.get_min())

    def pop(self):
        if len(self.data) == 0:
            raise StackEmptyError('Stack Empty! No Element Pop!')

        self.min_stack.pop()
        return self.data.pop()

    def top(self):

        if len(self.data) > 0:
            return self.data[len(self.data) - 1]

        raise StackEmptyError('Stack Empty!')


class StackEmptyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())

    min_stack.pop()
    print(min_stack.get_min())