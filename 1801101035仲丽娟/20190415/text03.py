#3、编程实现回文数判断。
#输入：abcdcba
#输出：True

#1一分为二，左边所有字符入栈，右边所有字符入队列
#2栈（左）和队列（右）依次各出一个元素
#左边元素！=右边元素，不是回文
#3当栈为空且队列为空就是回文


str = 'abcdcba'
stack = []
for i in str:
    stack.append(i)

stack2 = []
while len(stack) is not 0:
    stack2.append((stack.pop()))

a = ''.join(stack2)
if a == str:
    print(True)
else:
    print(False)
