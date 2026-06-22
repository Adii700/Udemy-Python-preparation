# Implicite type conversion 
# int + int = int
# int + float = float
# float + float = float
# float + int = int 
# str + int = error 
# str + float = error
 
''' python data type automatically convert one data to another data
'''
a = 19 # int 
b = 29.4 # float
c = a + b # float
'''
print(type(a))
print(type(b))
print(type(c))
'''

#Explicite type conversion
''' 
user convert data type 
'''
a = 39
b = '57'
c = int(b)
d = a + c 
print(d)
print(type(d))
