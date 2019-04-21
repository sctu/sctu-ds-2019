# 编程实现回文数判断
# 1,一分为二，
#  左边所有字符入栈，右边所有字符入队列

# 2，栈和队列依次各出一个元素
#  左边元素   不等于   右边元素，则不是回文

# 3，当栈为空，且队列为空，那就是回文

str = input("please input something:")
original = []
inverted = []
for i in str:
    original.append(i)

while len(original) != 0:
    inverted.append(original.pop())

for i in str:
    original.append(i)

if original == inverted:
    print("True")
else:
    print("False")