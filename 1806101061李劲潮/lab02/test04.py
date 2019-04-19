
#一个数据存储栈
def init(stack):
    stack.l = []

#操作栈
def push(stack, x):
    if x is None:
        pass
    else:
        stack.l.append(x)


def pop(stack):
    if stack.l is None:
        return '出现错误啦！'
    else:
        stack.l.pop(-1)


def top(stack):
    if stack.l is None:
        return '出现错误啦！r'
    else:
        return stack.l[-1]


def getMin(stack):
    if stack.l is None:
        return '出现错误啦！'
    else:
        return min(stack.l)
'''
双栈解决寻找最小元素的问题，其实就是:

进栈比大小，小则为min，同时压入，大则不压入储存栈；
出栈时，相比较，同则同出，为min，反之不操作。
'''