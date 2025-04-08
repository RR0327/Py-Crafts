"""
import json
#some json
Sixteen_Batch = '{"Cr":"Rohan","Id" : 32}'
#parse secA
secA = json.loads(Sixteen_Batch) #loads = Convert from JSON to Python
#result in python dictionary 
print(secA["Cr"])

#python obj[dict]
x = {
    "name":"Rakib",
    "age":24,
}
#convrtr into json
y = json.dumps(x) #dumps = Convert from Python to JSON
#result in json string
print(y)
"""

"""
Convert Python obj into json string

dict
list
tuple
string
int
float
True
False
None
""" 

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript Object Notation) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null
"""
"""
import json  

# Correcting the JSON string.  
x = '{ "name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null ,"cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}'  

# Convert to JSON:  
y = json.loads(x)  # This will now work correctly  

# Display the resulting dictionary  
print(y)  

# Accessing values correctly, assuming we want to print specific elements from the JSON  
print(y["name"])            # Access name  
print(y["cars"])           # Access cars  
print(y["children"])       # Access children  
print(json.dumps("hello"))  # String needs to be serialized to JSON format  
print(json.dumps(42))       # Integer needs to be serialized to JSON format  
print(json.dumps(31.76))    # Float needs to be serialized to JSON format  
print(json.dumps(True))      # Boolean needs to be serialized to JSON format  
print(json.dumps(False))     # Boolean needs to be serialized to JSON format  
print(json.dumps(None))      # None needs to be serialized to JSON format

"""

"""
                                                #Python         JSON
print(json.dumps({"name": "John", "age": 30}))  #dict           Object
print(json.dumps(["apple", "bananas"]))         #list           Array
print(json.dumps(("apple", "bananas")))         #tuple          Array
print(json.dumps("hello"))                      #string         String
print(json.dumps(42))                           #int            Number
print(json.dumps(31.76))                        #float          Number
print(json.dumps(True))                         #True           true
print(json.dumps(False))                        #False          false
print(json.dumps(None))                         #None           null

"""

"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent = 4))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

print(json.dumps(x, indent=4, sort_keys=False))

"""
"""
import re

txt = "The \t rain \n in Spain"
x = re.split("\s", txt)
print(x)
x = re.split("\t", txt)
print(x)
x = re.split("\n", txt)
print(x)
"""

"""
#maxsplit()
import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

"""

