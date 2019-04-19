a="{[()]}"
left="{[("
right="}])"
s=[]
for i in a:
    if i is "{"or\
        i is "["or\
        i is "(":
        s.append(i)
    elif i is "}"or\
        i is "]"or\
        i is ")":
        s.pop()
if a:
    print(True)
else:
    print(False)