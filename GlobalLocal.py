# Local Variable
'''
def hello():
    x = "hello" 
    print(x)
hello()

def hello():
    x = "hello" 
    print(x)
hello()
print(x) # error

'''

# Global Variable
'''
def hello():
    global y
    y = "hello" 
    print(y)
hello()

def hello():
    global y
    y = "hello" 
    print(y)
hello()
print(y)

def hello():
    global y
    y = "hello" 
    print(y)
def hello1():
    print(y)
hello()
hello1()
print(y)
'''