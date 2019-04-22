import random
numbers = [5, 10, 15, 20, 25]
print ("Original list : ",  numbers)
new_list = random.sample(numbers, len(numbers))
print ("List after not in-place shuffle  : ",  new_list)