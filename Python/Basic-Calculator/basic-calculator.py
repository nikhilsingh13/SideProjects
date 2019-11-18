# -*- coding: utf-8 -*-
"""
Author: Nikhil Singh
Date: November 18, 2019
Details: Basic Calculator which works mostly like a normal calculator.
Dependency: `re` library
"""

import re

previous=0
run=True

# function which performs the calculation
def performMath():
    global run
    global previous
    
    equation=""
    
    if previous==0:
        equation=input("Enter equation:")
    else:
        equation=input(str(previous))
    
    
    if 'quit' in equation:    # checking termination condition
        print("Bye Bye.... Closing Calculator..!")
        run=False
    else:
        equation=re.sub('[a-zA-Z,_:&()" "]',"",equation)  # eval safe coding practice, though python already stops a lot.
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous) + equation)
    print("Answer:",previous)


# Function to call to make calculator work endlessley unless passed `quit` as an input.
while run:
    performMath()