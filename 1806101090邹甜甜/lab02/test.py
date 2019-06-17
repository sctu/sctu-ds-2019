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
    print(reverse_str('Hello,World!'))

