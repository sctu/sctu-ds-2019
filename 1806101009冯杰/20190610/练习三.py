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