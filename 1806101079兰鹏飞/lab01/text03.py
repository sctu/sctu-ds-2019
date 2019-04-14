#3、编程实现回文数判断。
#
#输入：abcdcba
#
#输出：True

n=input()
stack=[]
for i in range(0,int(n)):
    stack.append(i)
    a=stack
    stack.pop()
    b=stack
if a==b:
    print("Ture")
else:
    print("False")