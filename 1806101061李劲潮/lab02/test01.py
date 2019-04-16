text='Hello,World!'

#定义函数
def exchange(text):
    stack=[]
    #push
    for i in text:
        stack.append(i)
    while len(stack) != 0:
    #pop
        print(stack.pop(),end="")

exchange(text)
