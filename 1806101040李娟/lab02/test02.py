#编程实现括号匹配

st = []
friends = input("请输入:")
for i in friends:
    if i=="("and"{"and"[":
        st.append(i)
    if i==")"and st[-1]=="(":
        st.pop()
    if i=="}"and st[-1]=="{":
        st.pop()
if len(st)==0:
    print("True")
else:
    print("Flase")
