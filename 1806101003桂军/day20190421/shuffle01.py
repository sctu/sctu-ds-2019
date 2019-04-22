import random
string_list = ["Paint It Black","Gimme Shelter","同情魔鬼","满意","你不能总是得到你想要的东西"]
print("原始字符串列表：",string_list)
random.shuffle(string_list)      #shuffle方法
print("第一次shuffle之后的字符串列表：",string_list)
random.shuffle(string_list)
print("第二次shuffle后的字符串列表：",string_list)