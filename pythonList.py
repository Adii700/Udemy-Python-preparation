
# empty list
'''
empty = []
print(empty)
'''

# list of int 
'''
a_list = [1, 3, 2]
print(a_list)
'''

#list of float
'''
a_float = [1.3, 3.4, 2.6]
print(a_float)
'''

#list of str 
'''
a_str = ["pineapple, gavava, blackberry"]
print(a_str)
'''
# list with mixed datatype
'''
mix = [2, 3.4, "sun"]
print(mix)
'''

# If we want print one value in this case 
'''
mix = [2, 3.4, "sun"]
print(mix) # [2, 3.4, "sun"]
'''

# Access list item
'''
mix = [2, 3.4, "sun"]
print(mix[2]) # sun

mix = [2, 3.4, "sun"]
print(type(mix[2])) # str
'''

#nested list item
'''
nest = [1, 2.3, "adiyogi"]
print(nest) #[1, 2.3, "adiyogi"]

nest = [1, [23, 45,], "adiyogi"]
print(nest[1]) # [23, 45]

nest = [1, [23, 45,], "adiyogi"]
print(nest[1][1]) # 45
'''

#negative indexing
'''
neg = [1, 2, 3, 4, 5, 6, 7]
print(neg) #[1, 2, 3, 4, 5, 6, 7]

neg = [1, 2, 3, 4, 5, 6, 7]
print(neg[-4]) #4

'''

# for finding the length of the value
'''
a = [1, 3, 4, 2, 7, 9]
print(len(a)) # 6 
'''