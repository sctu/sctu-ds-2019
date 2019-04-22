'''
stack = []
for i in "Hello,world!":
    stack.append(i)

while len(stack)  != 0:
    a = stack.pop()
    print(a)

 stack = []
 for i in "Hello,world!":
     stack.append(i)
while len(stack)  !=0:
    a=stack.pop()
    print(a)



stack = []
#   if i == '{' or i == '[' or i == '(':
#        stack.append(i)
i=
LEFT=['{','[','(']
RIGHT=['}',']',')']

if i in LEFT:
    stack.append(i)
if i in RIGHT:
    a=i
    left = stack.pop()
    b=stack.pop()
 if a.index() == b.index()
 print(TURE)
 else print(FALSE)


    if LEFT.index(left) != RIGHT.index(i):
        print('不匹配！')
        break
    if len(stack) == 0:
        print('匹配')
    else:
        print('不匹配')


     if len(stack) == 0:
         print('不匹配')
*/

# 学生 ： 姓名张三 ，年龄18， 性别：男
name= 'zhangsan'
age = 18
gender = 'male'
'''

#构造函数
class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printInfo(self):
        print('name:{}'.format(self.name))
        print('age:{}'.format(self.age))
        print('gender:{}'.format(self.gender))

zs = Student('zhangyuxiang',19,'male')
zs.printInfo()
















