# 3、编程实现回文数判断。
# 输入：abcdcba
# 输出：True


a = input("请输入abcdcba:")  #数据的输入

x = str(a)
flag = True

for i in range(len(x)/2):   #实现过程
    if x[i]!= x[-i-1]:
        flag = False
        break
#         range()函数返回的是可迭代对象，如果需要遍历一个数字序列，可以使用range对象。
#         eg:for i in range(5):
#                 print(i,end='')        程序输出结果为0 1 2 3 4


if flag:                    #输出过程
    print(True)

else:
    print(False)
