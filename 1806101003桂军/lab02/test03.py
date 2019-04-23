# 编程判断回文数
a = input("请输入数字: ") # 请输入一个数字
b = len(a)                  # 遍历这个数字的长度，并且将b赋值于a的长度
for i in range (b):      # 将b的每一项
    if(a[i]==a[b-i-1]):
        c=1
    else:
        c=0
if(c==1):
    print("Ture")
else:
    print("False")
