
# append()
'''
fruit = ["pineapple", "gavava", "jerry"]
print(fruit)
fruit.append("grapes")
print(fruit)
'''

# extend()
'''
lang = ["Hindi", "Gujrati", "Bangali"]
print(lang) # ["Hindi", "Gujrati", "Bangali"]
lang1 = ["Marathi"]
print(lang1) # ["Marathi"]
lang.extend(lang1)
print(lang) #["Hindi", "Gujrati", "Bangali", "Marathi"]
'''

# extend() use both [ + = ]
'''
lang = ["Hindi", "Gujrati", "Bangali"]
print(lang) # ["Hindi", "Gujrati", "Bangali"]
lang1 = ["Marathi"]
print(lang1) # ["Marathi"]
lang1 += ["Rajesthani"] 
lang.extend(lang1)
print(lang) #["Hindi", "Gujrati", "Bangali", "Marathi", "Rajesthani"]
'''

#lang.extend(lang1+ "Rajesthani")
#print(lang) # error

# extend()
'''
lang = ["Hindi", "Gujrati", "Bangali"]
print(lang) # ["Hindi", "Gujrati", "Bangali"]
lang1 = ["Marathi"]
print(lang1) # ["Marathi"]
lang1.extend(lang)
print(lang1) #["Marathi", "Hindi", "Gujrati", "Bangali",]
'''

#index() is use find the position the value
'''
lang = ["Marathi", "Hindi", "Gujrati", "Bangali",]
print(lang)
print(lang.index("Gujrati"))
'''

#insert() is use to add value according to their position
'''
lang = ["Marathi", "Hindi", "Gujrati", "Bangali",]
lang.insert(1, "Rajesthani")
print(lang) # ['Marathi', 'Rajesthani', 'Hindi', 'Gujrati', 'Bangali']
'''

#count() is use to count the number of value how many repeat 
'''
list_am = [3,2,4,2,4,5,5,9,5,]
print(list_am.count(5))

list_am = [3,2,4,2,4,5,5,9,5,]
print(list_am)
print(list_am.count(5))
print(type(list_am.count(5)))
'''

# remove() is use to remove the particular item in value
'''
lang = ["Marathi", "Hindi", "Gujrati", "Bangali",]
print(lang)
lang.remove("Hindi")
print(lang)
'''

#pop() is use to remove the particular position in value
'''
lang = ["Marathi", "Hindi", "Gujrati", "Bangali",]
print(lang)
lang.pop(2)
print(lang)
'''

# reverse() is used for reverse the value in the item
'''
lang = ["Marathi", "Hindi", "Gujrati", "Bangali",]
print(lang)
lang.reverse()
print(lang)
'''

# sort() is use to arrange the value in assending order
#Assending order
'''
a = [1, 45, 56, 3, 34]
print(a)
a.sort()
print(a)
'''
# Decending order 
'''
a = [1, 45, 56, 3, 34]
print(a)
a.sort(reverse=True)
print(a)
'''
