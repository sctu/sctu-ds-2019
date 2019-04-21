# import random
# string_one = "pynative"
# random.shuffle(string_one)
# print(string_one)
import random
string_one = "pynative"
print ("Original String: ", string_one)
char_list = list(string_one) # convert string inti list
random.shuffle(char_list) #shuffle the list
string_one = ''.join(char_list)
print ("shuffled String is: ", string_one)