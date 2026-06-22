# Set is always using {} and also asscending form
'''
my_set = {1,2,7,5,3,9}
print(my_set)

my_new = {1,1.0, "Adiyogi"}
my_new1 = {1,3.0, "Adiyogi"}
my_new2 = {1,1.0, "Adiyogi",2,2}
print(my_new) # {1, 'Adiyogi'}
print(my_new1) # {1, 3.0, 'Adiyogi'}
print(my_new2) # {1, 2, 'Adiyogi'}
'''

# this call error because the set is not support indexing[]
'''
a = {"a","b","c"}
print(a) # {'a', 'b', 'c'}
print(a[0]) 
'''

# for add single value
'''
my_set = {1,2,7,5,3,9}
my_set.add(4) 
print(my_set)
'''

# for add multiple value/ update
'''
my_set = {1,2,7,5,3,9}
my_set.update([6,8,5,10,11])
print(my_set) # {1, 2, 3, 5, 6, 7, 8, 9, 10, 11}
'''

# for remove single value
'''
my_set = {1,2,7,5,3,9}
my_set.remove(2)
print(my_set) # {1, 3, 5, 7, 9}
'''

# Set Oparation
# Union - sets of all elements in both with assending order
'''
a = {0,1,8,4}
b = {5,6,7}
print(a|b) # {0, 1, 4, 5, 6, 7, 8} 
'''

# Intersection - elements that are comman
'''
a = {0,56,78,33}
b = {0,78,33}
print(a&b) # {0, 33, 78}
'''

# for check when in one item 2 value are same then remove one or two value
'''
my_name = {1,2,4,2,7,5}
my_name.remove(2)
print(my_name) # {1, 4, 5, 7}
'''

#for check when in one item 2 value are same then print one time or two times 
'''
a = {1,2,4,2,5}
b = {3,2,9,5,1}
print(a&b) #{1, 2, 5}
'''