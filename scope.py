'''
@ASSESSME.USERID: mk8763
@ASSESSME.AUTHOR: Matej Korpar
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

##I WANTED TO COPY PASTE GLOBAL VARIABLES FROM THE DOCX THAT WE ARE PROVIDED!!! just in case

STRING_GLOBAL = "Hi"
INT_GLOBAL = 6
FLOAT_GLOBAL = 9.13

def print_param(sanemi):
    return print(sanemi)

def print_local():
    giyu = "GIYU IS SO COOL"
    return print(giyu)

def print_which():
    INT_GLOBAL = "Sanemi is my favourite tho"
    return print(INT_GLOBAL)


def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)
    
    sanemi = "he is my number 1"
    print_local()
    print_which()

if __name__ == "__main__":
    main()