# Dictionary
'''
my_dict = {"car": "swift", "game": "car game"}
print(my_dict) # {'car': 'swift', 'game': 'car game'}
print(my_dict.keys()) #dict_keys(['car', 'game'])
print(my_dict.values()) # dict_values(['swift', 'car game'])
print(my_dict["game"]) # car game
print(my_dict["car"]) # swift
'''

my_dict = {"Car":["swift","braza","i10","verna"], "Game":["car game","bike game","batminton","cricket"]}
'''
print(my_dict) #{'Car': ['swift', 'braza', 'i10', 'verna'], 'Game': ['car game', 'bike game', 'batminton', 'cricket']}
print(my_dict.keys()) # dict_keys(['Car', 'Game'])
print(my_dict.values()) # dict_values([['swift', 'braza', 'i10', 'verna'], ['car game', 'bike game', 'batminton', 'cricket']])
print(my_dict["Car"]) # ['swift', 'braza', 'i10', 'verna']
print(my_dict["Game"]) # ['car game', 'bike game', 'batminton', 'cricket']
'''
print(my_dict["Car"][0]) # swift
print(my_dict["Car"][2]) # i10
print(my_dict["Game"][0]) # car game
print(my_dict["Game"][3]) # cricket