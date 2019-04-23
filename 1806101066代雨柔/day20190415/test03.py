#3、编程实现回文数判断
t='abcdcba'
#1）一分为二
left=['abc']
right=['cba']
#   左边所有字符入栈，右边所有字符入队列
stack=[]
for i in 'abc':
    stack.append(i)
queue=[]
for l in 'cba':
    queue.append(l)

#2）栈和队列依次各出一个元素
a=stack.pop(i)
b=queue.pop(l)
#   左边元素！=右边元素    不是回文
if a!=b:
    print('不是回文')
#3）当栈为空队列为空就是回文
if len(a)=0
if len(b)=0


#输入'abcdcba'
#输出'True'