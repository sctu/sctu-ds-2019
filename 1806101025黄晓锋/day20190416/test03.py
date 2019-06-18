#回文判断
#输入字符
#将字符均分成两段
#左边一段压栈
#右边进队列
#出栈，出队列并比较
#若匹配，则输出True
#若不匹配，则输出False
'''编程实现回文数判断。

输入：abcdcba

输出：True'''

def huiwenshu(s):
    if len(s) < 2:
        return False
    if s[0] == s[-1]:
        return True
    else:
        return False
s1 = 'abcdcba'
s2 = '1234'
print(huiwenshu(s1))
print(huiwenshu(s2))