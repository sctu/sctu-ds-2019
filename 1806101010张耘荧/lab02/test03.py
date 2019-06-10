# 编程实现回文数判断。
# 输入：abcdcba
left = []
right = []
s = input("请输入：")
a = int(s)

# 1. 一分为二，左边进栈，右边进队列。
for i in s(0 , 1/2 * a):
    left.append(i)
for j in s(1 / 2 * a , a):
    right.append(j)


# 2. 左边出一个字符，
#    右边出一个字符，进行比较。
while a == 0:
    if left.pop() == right.pop():
        print("True")
    else:
        print("False")


# 3. 三种情况处理
# (1) 左边栈为空，右边队列不为空
# (2) 左边栈不为空，右边队列为空
# (3) 左边栈和右边队列都为空