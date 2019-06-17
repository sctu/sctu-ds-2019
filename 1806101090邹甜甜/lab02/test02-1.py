LEFT = ['(','[','{']
RIGHT = [')',']','}']

def parentheses_mach(input_str):
    stack = []

    for ch in input_str:
        if ch in LEFT:
            stack.append(ch)
        elif ch in RIGHT:

            if len(stack) > 0 and RIGHT.index(ch) ==LEFT.index(stack.pop()):
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
    print(parentheses_mach('{[()]}'))

