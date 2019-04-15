str=input('请输入括号：')
if len(str)%2!=0:
    print('匹配失败！')

brackets={'[':']','(':')','{':'}'}
stack=[]

