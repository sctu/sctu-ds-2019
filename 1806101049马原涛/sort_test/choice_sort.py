ls=[53,22,87,12,65,47,55,20,5,43,33,75]
minValue=0
for j in range(0,len(ls)-1):#实际遍历从0到n-2，共n-1次

    for i in range(j+1,len(ls)):#从j+1到最后一个元素

        if ls[i]<ls[minValue]:
            minValue = i#记录最小值下标，不要急着交换位置，后面仍然可能存在更小的值

        if i==len(ls)-1:#内层循环遍历到最后一个元素，表示本次循环即将结束，本次循环最小值已确定，可以交换位置了

            ls[j],ls[minValue]=ls[minValue],ls[j]#交换位置后，最小值下标仍然是交换位置前的下标，但现在交换位置后，需要重置

            minValue=j+1#对最小值下标进行重置

print(ls)