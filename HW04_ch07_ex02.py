#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math

#Body

def eval_loop():
    last_evaluation = "N/A"
    while True:
        try:
            evaluation = (input("What would you like to evaluate? "))
            if evaluation == ("done"):
                return last_evaluation
            last_evaluation = eval(evaluation)
            print(last_evaluation)

        except:
            print("Sorry, I can only evaluate mathematical expressions")
    

###############################################################################
def main():

    print(eval_loop())

if __name__ == '__main__':
    main()
