# 4、编程实现MinStack.
stack=[]
MinStack=[]
minIndex=0
def once(stack, MinStack, minIndex, shuru):
    stack.append(shuru)
    MinStack.append(shuru)
    minIndex=shuru
    return minIndex
def Min(stack, MinStack,  minIndex,shuru):
    minIndex=MinStack[-1]
    if shuru < minIndex:
        stack.append(shuru)
        minIndex = shuru

        MinStack.append(minIndex)
    else:
        stack.append(shuru)
        MinStack.append(minIndex)

while True:
    shuru = eval(input('请输入一个值压栈：'))
    if len(stack)==0:
        once(stack, MinStack, minIndex, shuru)
    else:
        Min(stack, MinStack, minIndex, shuru)
    print('最小值为%d'%MinStack[-1])
    print('栈内元素{}\n最小栈元素{}'.format(stack,MinStack))






