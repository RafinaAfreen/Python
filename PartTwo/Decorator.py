s = "Global variable"

def func():
    #return 1
    #global s
    #s=50
    #print(s)
    mylocal = 10
    print(locals())
    print(globals()['s'])
func()
print(s)

def hello(name="Rafina"):
    return "hello "+name

print(hello())

mynewgreet = hello

print(mynewgreet())

def hello1(name="Rafina"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"

    if name == "Rafina":
        return greet
    else:
        return welcome
    #print(greet())
    #print(welcome())
    #print("End of hello()")

x = hello1()
print(x())


def hello2():
    return "Hi Rafina"

def other(func):
    print("hello")
    print(func())

other(hello2)

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FINC() HAS BEEN CALLED")

    return wrap_func
@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

#func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()
