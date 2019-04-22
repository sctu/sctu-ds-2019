stack = []


friends = input("请输入:")
for i in friends:
    if i=="("and"{"and"[":
        stack.append(i)
    if i==")"and stack[-1]=="(":
        stack.pop()
    if i=="}"and stack[-1]=="{":
        stack.pop()
    if i=="]"and stack[-1]=="[":
        stack.pop()
if len(stack)==0:
    print("True")
else:
    print("Flase")