str = "{[()]}"
stack = []
Left = "{{("
Right = "})}"
R = []

for i in str:
    if i in Left:
        stack.append(i)
        print(i)
    else:
        R = stack.pop()
        print(R)
        right_index = Right.index(R)
        left_index = Left.index(i)
        if left_index != right_index:
            print('Wrong')
            break
if len(stack) is 0:
    print('True')
else:
    print('Wrong')






