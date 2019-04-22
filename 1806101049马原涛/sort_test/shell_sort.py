alist=[53,25,92,19,78,30,43,56,21]
gap=len(alist)
while gap>=1:   #控制步长
    gap=gap//2  #当步长为4时、当步长为2时、当步长为1时、都需要进行排序操作
    for j in range(gap,len(alist)): #执行多个序列间的比较
            # 比较完序列1第一位（gap），就比较序列2第二位（gap+1）.......
        i=j

        while i>0:  #该循环为同序列比较
            if alist[i]<alist[i-gap]:   #后一位与前一位作比较
                alist[i],alist[i-gap]=alist[i-gap],alist[i]
                i-=gap  #当i=0终止循环的条件，同一行需要比较两次以上时，需要更改比较对象
                    #如序列1：53、78、21 | 21在于78比较完后，还需要于53做比较
            else:
                break

print(alist)