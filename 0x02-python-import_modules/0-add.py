#!/usr/bin/python3
from add_0 import add

#Here is empty code so when you import this module into anthor module
#the global variable __name__is"__this_module_name_itself__"
#so it print nothing

if __name__ == "__main__":
    #when you run this module directly like ./0-add.py or python3 0-add.py
    #the global variable __name__ is "__main__"
    #then this module is executed as ascript
    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
