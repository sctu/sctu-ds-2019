#3、编程实现回文数判断。
#
#输入：abcdcba
#
#输出：True

n=input()
stack=[]
huiwen=''
for i in range(0,len(n)):
    stack.append(n[i])
for i in range(0,len(n)):
    a=stack.pop()
    huiwen+=a
if huiwen==n:
    print("Ture")
else:
    print("False")