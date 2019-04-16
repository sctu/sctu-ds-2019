#编程实现MinStack.
from math import *
stack1=[]
stack2=[]
#将元素进行压栈
for i in range(1,10):
    stack1.append(i)
# 将元素进行压栈
    if i<i+1:
        stack2.append(i)
    else:
        stack1.append(i)
 # 如果小于之前的元素，出到一个最小栈，如果大于 继续压栈
print(min(stack2))

#在最小栈中取得最小值
