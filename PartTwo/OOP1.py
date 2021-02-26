myclass = [1,2,3]
myclass.append(4)
print(myclass)

print(type(200))
print(type([1,2,3]))
print(type(20.4))

class Sample(object):
    pass

x = Sample()
print(type(x))

class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog("Lab","Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi
    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.area())


class Animal():
    def __init__(self):
        print ("Animal created")

    def whoAmI(self):
        print ("Animal")

    def eat(self):
        print ("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")

    def whoAmI(self):
        print ("Dog")

    def bark(self):
        print ("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

class Book():
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print ("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print (book)
print (len(book))
del (book)
