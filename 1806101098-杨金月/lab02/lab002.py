str = "{[()]}"
stack=[]
l = []
Left = "{{("
Right = "})}"
r = []

for i in str:
    if i in Left:
        stack.append(i)
        print(i)
    if i in Right:
        r = stack.pop()
        print(r)
    right_index = Right.index(" ".join(r))

    left_index = Left.index(i)

    if left_index != right_index:
        print("wrong")
        break

if len(stack) is 0:
    print("true")
else:
    print('wrong')


