# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。
# 1、请输入一个正整数
n = input("请输入一个正整数：")
sum = 0
k = 0
result = ''
for chr in n:   #遍历每一项并求和
    sum = sum+int(chr)
str_sum = str(sum)
for chr1 in str_sum:
    if(chr1 == '1'):
        result += 'yi'
    if(chr1 == '2'):
        result += 'er'
    if(chr1=='3'):
        result += 'san'
    if(chr1=='4'):
        result += 'si'
    if(chr1=='5'):
        result += 'wu'
    if(chr1=='6'):
        result += 'liu'
    if(chr1=='7'):
        result += 'qi'
    if(chr1=='8'):
        result += 'ba'
    if(chr1=='9'):
       result += 'jiu'
    if(chr1=='0'):
       result += 'ling'

    k = k+1
    if k != len(str_sum):
        result += ' '
print(result)

