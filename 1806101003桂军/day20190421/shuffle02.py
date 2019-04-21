import random
numbers = [10, 20, 30, 40, 50, 60]
print ("Original list: ", numbers )
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)

numbers = [10, 20, 30, 40, 50, 60]
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)