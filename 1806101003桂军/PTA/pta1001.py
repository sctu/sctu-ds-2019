# 1、先输入一个正整数n
n = eval(input("请输入一个正整数："))
if n>1000:
    print("我是小笨笨，算不出来这么大的")
else:
    cut = 0
    while n !=1:   #如果x不等于1则继续循环
        #判断是奇数还是偶数
        if (n%2 == 0):  #如果为偶数则砍掉一半
            n = n/2
        else:
            n = (3*n+1)/2  #如果是奇数则（3n+1）再砍掉一半
        cut = cut + 1
    print(cut)