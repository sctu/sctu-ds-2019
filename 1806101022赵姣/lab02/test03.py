#回文

num=input("输入一个数")
if num.isdigit():
    num=str(num)
    for i in range(len(num)//2):
        if num[i]==num[len(num)-i-1]:
            print("True")
        else:
            print("False")