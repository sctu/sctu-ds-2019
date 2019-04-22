# 1. 一分为二
#   左边所有压栈 右边入队列
# 2.栈和队列 一次各出一个元素
#   左边的元素 ！= 右边的元素 则不是回文
# 3.当栈为空且队列为空时 则是回文
# 编程实现回文数判断。
# #
# # 输入：abcdcba
# 输出：True
stack = []
queue = []
for i in "abcdcba":
    if i in 'abc':
        stack.append(i)
    if i in 'cba':
        queue.append(i)

def check(r1,r2):
    r1=stack.pop(i)
    r2=queue.pop(i)

while stack and queue is 0:
    print("true")
else:
    print("false")






