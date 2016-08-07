# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.


#################################################################
# Body
def rotate_word(word, integer):
    new_word = ''
    for char in word:
        if char.islower():
            if ord(char) + integer > 122:
                rotation = chr(ord(char) + integer - 26)
                new_word += rotation
            elif ord(char) + integer < 97:
                rotation = chr(ord(char) + integer + 26)
                new_word += rotation
            else:
                rotation = chr(ord(char) + integer)
                new_word += rotation
        else:
            if ord(char) + integer > 90:
                rotation = chr(ord(char) + integer - 26)
                new_word += rotation
            elif ord(char) + integer < 65:
                rotation = chr(ord(char) + integer + 26)
                new_word += rotation
            else:
                rotation = chr(ord(char) + integer)
                new_word += rotation
    print(new_word)


#################################################################
def main():

    rotate_word("cheer", 7)
    rotate_word("zebra", 7)
    rotate_word("Zebra", 7)

if __name__ == '__main__':
    main()