def revere_str(input_str):
    stack = []
    target = []

    for i in input_str:
        stack.append(i)

    while len(stack) != 0:
        target.append(stack.pop())
    return target


if __name__ == '__main__':
    print(revere_str('Hello,World!'), end='')