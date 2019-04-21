# 编程实现回文数判断。
# 输入:a b c d c b a
# 输出：True

# 1.一分为二，左边字符入栈，右边字符入队列
stack = []
queue = []
LEFT = ['a', 'b', 'c']
RIGHT = ['c', 'b', 'a']
for i in 'a b c d c b a':
    if i in LEFT:
        # print(i)
        stack.append(i)
    if i in RIGHT:
        queue.append(i)
# 2.栈和队列依次各出一个元素
# 左边元素 ！= 右边元素 不是回文
if LEFT !=RIGHT:
    print('不是回文')
# 3.当栈为空且队列为空，就是回文
else:
    print('是回文')
