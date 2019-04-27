#用递归计算某数的阶乘
# def a(n):
#     if n==0:
#         return 1
#     else:
#         return n*a(n-1)
# mum=eval(input('请输入一个整数：'))
# print(a(abs(int(mum))))


#用递归画ckhe曲线
# from turtle import *
# setup(500,500)
# color('white','white')
# bgcolor('blue')
# def quxian(q,w):
#     if w==0:
#         fd(q)
#     else:
#         for angle in [0,60,-120,60]:
#             left(angle)
#             quxian(q/3,w-1)
# def shuru():
#     e=eval(input('请输入前进长度：'))
#     r=eval(input('请输入前进阶数：'))
#     return e,r
# t,y=shuru()
# def xuehua(m,n):
#     quxian(m,n)
#     right(120)
#     quxian(m,n)
#     right(120)
#     quxian(m,n)
# begin_fill()
# xuehua(t,y)
# end_fill()
# penup()
# goto(-130,-100)
# pendown()
# begin_fill()
# xuehua(t-60,y-1)
# end_fill()
# hideturtle()
# done()