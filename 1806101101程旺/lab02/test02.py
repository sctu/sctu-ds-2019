#括号匹配
kh = []
yourInput = input("please input something:")
for i in yourInput:
    if i=="("and"{"and"[":
        kh.append(i)
    elif i==")"and kh[-1]=="(":
        kh.pop()
    elif i=="}"and kh[-1]=="{":
        kh.pop()
    elif i=="]"and kh[-1]=="[":
        kh.pop()
if len(kh)==0:
    print("match")
else:
    print("unmatch")