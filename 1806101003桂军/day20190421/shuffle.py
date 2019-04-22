import random
number_list = [7,14,21,28,35,42,49,56,63,70]
print("原始列表：",number_list)

random.shuffle(number_list)   #shuffle方法
print("first shuffle：之后的列表：",number_list)

random.shuffle(number_list)
print("第二次洗牌之后列出：",number_list)