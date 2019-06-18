# 编程实现字符串反转

#输入：Hello,World!

#输出：!dlroW,olleH

def reverse_str(input_str):
    stack = []
    target = []

    for ch in input_str:
        stack.append(ch)

    # 出栈直到栈为空为止，并且打印每一个字符
    while len(stack) != 0:
        ch = stack.pop()
        target.append(ch)

    return target

if __name__ == '__main__':
    reverse_str('Hello,World!')

