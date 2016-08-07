#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Nothing wrong"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Quotations should not be present - True and False are registered as
    strings rather than booleans; moreover, by using the quotation marks
    around the letter c python evaluates c as a character rather than a function"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """True or false are assigned only based on the last letter of the word"""
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Nothing wrong"""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Once the script runs into an upper case letter it stops the loop
    and returns False"""
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    print(any_lowercase2("HERE"))

    print(any_lowercase3("herE"))

    print(any_lowercase5("hERe"))

if __name__ == '__main__':
    main()
