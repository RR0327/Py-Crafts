"""

class SecA:
    name = ""
    id = ""
    term = ""

rohan = SecA()
#print(isinstance(rohan,SecA))
rohan.name = "Rohan"
rohan.id = 32
rohan.term = 1
print(f"Name : {rohan.name}  \nId No : {rohan.id}  \nTerm : {rohan.term}")

javed = SecA()
#print(isinstance(javed,SecA))
javed.name = "Javed"
javed.id = 43
javed.term = 1
print(f"Name : {javed.name}  \nId No : {javed.id}  \nTerm : {javed.term}")





class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Mike Olsen


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#2019



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

"""
"""
#Build in function 4 types : list,tuple,set,dictionary

# List example  
my_list = [1, 2, 3]  
list_iterator = iter(my_list)  # Get iterator  
print(next(list_iterator))  # Output: 1  

# Tuple example  
my_tuple = (4, 5, 6)  
tuple_iterator = iter(my_tuple)  
print(next(tuple_iterator))  # Output: 4  

# Dictionary example  
my_dict = {"key1": "value1", "key2": "value2"}  
dict_iterator = iter(my_dict)  # Iterates over keys by default  
print(next(dict_iterator))  # Output: "key1"  

# Set example  
my_set = {7, 8, 9}  
set_iterator = iter(my_set)  
print(next(set_iterator))  # Output: 7 (order may vary since sets are unordered)

"""

"""import re 
for i in dir(__builtins__):
    if re.match(r'^[A-Z]',i):
        print(i)"""

"""# Normal Code
class glass:
    pass
class shader:
    def index(self):
        print("Hint")

class sunglass(glass, shader):
    pass

obj = sunglass()
obj.index()"""

