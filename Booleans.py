# Boolean Values

# Booleans represent one of two values: True or False.

# examples

print(10>5)

print(4>5)



# Evaluate Values and Variables

# the bool() function allows you to evaluate any value, and give you True or False in return

print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool("a"))



# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))



# Some Values are False
# In fact, there are not many values that evaluates to False,
# except empty values, such as (), [], {}, "", the number 0,
# and the value None. And of course the value False evaluates to False.

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



# One more value, or object in this case, evaluates to False,
#  and that is if you have an object that is made from a class
#   with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())


