# 3、编程实现回文数判断。
#
# 输入：abcdcba
#                                                                                                                    c
# 输出：True
str=input()
a=''
for i in range(1,len(str)+1):
    a+=str[-i]
if str==a:
    print('Ture')
else:
    print('False')

