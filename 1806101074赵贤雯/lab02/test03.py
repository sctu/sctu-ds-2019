# 输入： abcdcba
# 输出： true

# 1. 一分为二，左边进栈，右边进队列
str='abcdcba'
stack=[]
queue=[]
front=['a','b','c','d']
back=['c','b','a']
for i in str:
    print(i)
    if i in front:
        stack.append(i)
    else:
        queue.append(i)


# 2. 左边出一个字符，右边出一个字符，进行比较。


# 3. 三种情况处理
# （1） 左边栈为空，右边队列不为空
# （2） 左边栈不为空，右边队列为空
# （3） 左边栈右边队列都为空
