stack = []
str = '{[()]}'
Left = '{[('
Right = '}])'
for ch in str:
    print(ch)
    if ch is in 'Left':
        stack.append(ch)
    if ch is in 'Right':
        stack.append(ch)
