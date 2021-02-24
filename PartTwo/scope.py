x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#print(x)
#print(printer())
#print(x)


f = lambda x:x**2

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()

print (name)


x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

y = 50

def func():
    global y
    print('This function is now using the global y!')
    print('Because of global y is: ', y)
    y = 2
    print('Ran func(), changed global x to', y)

print('Before calling func(), y is: ', y)
func()
print('Value of y (outside of func()) is: ', y)
