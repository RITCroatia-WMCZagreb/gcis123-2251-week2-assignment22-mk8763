'''
@ASSESSME.USERID: mk8763
@ASSESSME.AUTHOR: Matej Korpar
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

def add_chars(char1,char2):
    n1 = ord(char1)
    n2 = ord(char2)
    added = chr(n1 + n2)
    print("Sum of", char1, "and", char2,"=", str(n1 + n2))
    return print("Character =", added)

def subtract_chars(char1,char2):
    n1 = ord(char1)
    n2 = ord(char2)
    if n1 > n2:
        subtr = n1 - n2
        new = chr(subtr)
    else:
        subtr = n2 - n1
        new = chr(subtr)
    print("Difference of", char1, "and", char2,"=", str(subtr))
    return print("Character =",new)

def main():
    value1 = input("Enter 1st character: ")
    value2 = input("Enter 2nd character: ")

    add_chars(value1,value2)
    subtract_chars(value1,value2)

if __name__ == "__main__":
    main()

'''
### COMMENT 1
- Sometimes i see odd characters that i do not see in ASCII table
and sometimes i see nothing at all. I assume that that happens since
some characters are not included in the ASCII table that we are provided 
in the slides and there are more characters since there is a lot of languages
and sometimes its empty because first 32 characters are unprintable since they are
control characters 

### COMMENT 2
- when i enter two characters it says: "TypeError: ord() expected a character, but string of length 2 found"
that happens because i use command ord() which can be used for only one character and not a string of length 2 or more


'''