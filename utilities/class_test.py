import cgi
from utilities import *
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    def a():
        return 'hello a'

print MyClass.i
#Doesnt work
#print MyClass.a()

obj = MyClass()
#Prints an object
print obj.a
print obj.i
#Error TypeError: a() takes no arguments (1 given), because self is not defined in the method
#print obj.a()
print obj.f()
print MyClass.f(obj)

#Possible because Classes are class objects !!!
MyClass.j = 10
print MyClass.j

def new_method(self):
    print "Hi..I am new method"

#Add a method later!!
MyClass.new_method =  new_method

#Call the new method dynamically !! WHOLA !! 
obj.new_method()

class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print range(9, -1, -1)
print range(0,10,2)