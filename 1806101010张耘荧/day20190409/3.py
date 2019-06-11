stack = []
queue = []
c = input("请输入回文数：")
num = stack.append(c)
a = int(1/2*c)
b = str(1/2*c)
for i in c:
    if len(c)%2 == 0:
        stack.pop(a)
        if stack.pop(a) is len(b):
            print("是回文数")
        else:
            continue
    elif len(c)%2 != 0:
        s = stack.pop(a)
        stack.pop(a+1)
        if stack.pop(a) is len(b):
            print("是回文数")
        else:
            print("不是回文数")


