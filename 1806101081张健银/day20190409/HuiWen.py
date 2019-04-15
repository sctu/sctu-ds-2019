# 3、编程实现回文数判断。
#
# 输入：abcdcba
#
# 输出：True
chars = "abcdcba"
stack = []
for i in chars:
    stack.append(i)
list = []
while len(stack) is not 0:
    n = stack.pop()
    list.append(n)
char = ""
for j in list:
    char += j
if char == chars:
    print("true")

else:
    print("false")
