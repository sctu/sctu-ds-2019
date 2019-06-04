
def text1(a):
    if (a%2==0):
        a = a/2
    elif (a%2!=0):
        a = (3*a+1)/2
    return a
a = int(input())
i = 0
while a>1:
    a = text1(a)
    i+=1
print(i)
