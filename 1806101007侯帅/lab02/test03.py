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




