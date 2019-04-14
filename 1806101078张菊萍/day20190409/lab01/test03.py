#
# 输入：abcdcba
#
# 输出：True
str=input()
a=''
for i in range(1,len(str)+1):
    a+=str[-i]
if str==a:
    print('Ture')
else:
    print('False')
