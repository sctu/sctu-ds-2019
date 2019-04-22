#括号匹配


ls = []
parens="{[()]}"
for i in parens:
    if i=="("and"{"and"[":
        ls.append(i)
    elif i==")"and ls[-1]=="(":
        ls.pop()
    elif i=="}"and ls[-1]=="{":
        ls.pop()
    elif i=="]"and ls[-1]=="[":
        ls.pop()
if len(ls)==0:
    print("True")
else:
    print("False")