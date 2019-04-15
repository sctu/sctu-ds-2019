a = input("请输入数: ")
b=len(a)
for i in range (b):
    if(a[i]==a[b-i-1]):
        c=1
    else:
        c=0
if(c==1):
    print("Ture")
else:
    print("False")
