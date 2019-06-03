"3.编程实现回文数判断。输入：abcdcba 输出：True

n=input()#输入字母 赋值
l=[]#列表
x=[]
for i in n:
    l.append(i)
for j in range(1,len(n)+1):#栈
    x.append(l[-j])
if l==x:
    print(True)
else:
    print(False)#(??也可不要)