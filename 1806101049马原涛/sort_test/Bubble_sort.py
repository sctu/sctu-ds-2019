#冒泡排序
ls=[53,22,87,12,65,47,55,20,5,43]
for j in range(0,len(ls)-1):
    for i in range(0,len(ls)-1-j):
        if ls[i] > ls[i+1]:
            ls[i],ls[i+1]=ls[i+1],ls[i]
print(ls)