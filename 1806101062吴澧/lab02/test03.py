# 1、一分为二
#    左边所有字符入栈，右边所有字符入队列
stack=[]
queue=[]
left=['a','b','c']
right=['c','b','a']
for i in 'abcdcba':
    if i in left:
        stack.append(i)
    if i in right:
        queue.append(i)
# 2、栈和队列依次各出一个元素
result=[]
for i in 'abcdcba':
    if i in left:
        result.append(stack.pop())
    if i in right:
        result.append(queue.pop())
print(result)
    # left_index=left.index(left_zimu)
#    左边元素  ！=右边元素  不是回文
#
# 3、当栈为空且队列为空，就是回文。