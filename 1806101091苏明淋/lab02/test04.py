class MinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []

    def get_min(self):
        return self.min_stack[len(self.min_stack) - 1]

    def push(self,num):
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

        def __init__(self,value):
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