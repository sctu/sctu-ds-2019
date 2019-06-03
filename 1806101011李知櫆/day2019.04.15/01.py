# 字符串反轉
# 輸入hello world!
# 輸出dlrow,olleh
# 字符串裏每一個字符進行壓棧
# 出棧直到棧為空爲止，打印每個出棧元素
stack=[]
for i in "hello,world!":
    stack.append(i)
while len(stack) ! = 0:
        print(stack.pop())
