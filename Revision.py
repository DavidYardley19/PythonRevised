print("Hello world!")

# this is a comment
""" 
This is a multi line string
"""

myNum = 5
myName = "David"
myBool = True
print(myNum, myName, myBool)

if myNum > 2:
    print(f"{myNum} is greater than 2")
else:
    print(f"{myNum} is not greater than 2")

# Type casting:
myFloat = 1.01
myFloatToInt = int(myFloat)
print(myFloatToInt)
# floating digits are lost since integers only support whole numbers

print("String variables can also be surrounded by 'single quotes'")

""" 
Variable names:
    You cannot have vars starting with a number
    It must start with a letter or an underscore
    They can only contain alphanumeric chars
    They are case sens
    Must not be any predefined keywords... like if, else, print, etc.

    bestToUseCamelCase or snake_case... But you can use all CAPS when defining constants
"""

# Multiple vars can be assigned simultaniously
x, y, z = 1,2,3
print(x)
print(y)
print(z)

# One val to multiple vars
x = y = z = 1
print(x)
print(y)
print(z)

""" Collection: values in a list, typle etc... You can extract these into vars... THIS IS UNPACKING """
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)
# I wonder though, do you need exactly the same amount of variables as elements in the collection?
""" a, b = fruits 
This would cause an error
"""

# Commas have been used before to print multiple variables, values and strings... This would typically leave a space after the last element
# You can also use the + symbol.. This would leave no space
print("Hello "+ myName)

# The + symbol is a mathematical operator
x = 1
y = 2
print(f"{x} + {y} =",(x+y))
# You cannot do this with different datatypes such as strings and integers...

""" 
Variables created outside of a function are known as global variables, local vars are the opposite
"""

x = "Awesome"
# defining funct
def MyFunction():
    x = "Brilliant" # This was created locally within the scope of the function so the initial value assigned to x globally remains unchanged.. Be careful!
    print("Python is " + x)
# Calling funct
MyFunction()
print("Python is " + x)

# You can have a little more control by using the global keyword within the scope of the function
def FunctionWithGlobal():
    global x
    # This creates a global function, it can also be used to amend global variables
    x = "Fantastic"

FunctionWithGlobal()
print("Python is " + x)

""" 
Built in data types
    Text Type     :	str
    Numeric Types :	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type  :	dict
    Set Types     :	set, frozenset
    Boolean Type  :	bool
    Binary Types  :	bytes, bytearray, memoryview
    None Type     :	NoneType

Ones that I have not heard of:
    complex
        x = 1j
    range
        x = range(6)
    frozenset
        x = frozenset({"apple", "banana", "cherry"})
    memoryview
        x = memoryview(bytes(5))
 """

print("The data type for nyName is" , type(myName))

# You can specify a specific data type for a variable in the same way that you type cast
x = int(12431324)
# These are called constructor functions

""" 
Numbers:
    int, float, complex

    int: whole pos and neg values... unlimited length
    float: same but contains one or more decimal points
    complex: This is the same as complex numbers in maths, with an imaginary part.
"""

# Float can also be assigned with the scientific e... indicating to the power of 10
myFloat = 1.23e1
# A capital E can also be used here, I prefer the lower case e since it stands out more from the 0-9 number set
print(myFloat)

myComplex = 12 + 5j
# I ABSOLUTELY despise that j is used instead of i... who came up with this idea to use j...... Really annoying.
# NOTE: you cannot convert complex values into other number types. What if there was no j part though.

myComplex = 12
complexToInt = int(myComplex)
print(complexToInt)
# Yes you can convert so long as there is no j part

""" Random: You will need to import random first """
import random
print(random.randrange(1,10))
# This will produce a random value between 1 and 9

""" More on casting
    You can cast a number variable into a string using the str() constructor
 """

print("It 'takes' a little",'work to "include" both single and double quotes in an output')

# multiline strings
a = """Hello
My name
Is Dave"""
print(a)

# Strings ARE arrays by the way... they are an array of bytes representing unicode chars >> I believe each character is up to 4 bytes long, whilst ascii is 1 byte long
print(a[0])
# indexing start from 0 remember

# You can loop through a string of chars
a = "12345"
for i in a:
    print(i)

# How to find the length of a string
print("There are" , len(a) ,"characters in the string:", a)

# You can check if a substring is contained within a string with the following:
print("123" in a)
if "123" in a:
    print("123 is present in the variable:",a)

if "6" not in a:
    print("6 is NOT present in the variable:",a)

""" 
Slicing: This is the same as indexing, but you can choose the range of characters to split up instead.
"""
b = "0123456789"
print(b[2:5])
# Remember that 5 is not included.

# You can also slice from the start or end by leaving the value blank
print(b[:5])
print(b[5:])

# Negative indexing is used to splice from the end of the string
print(b[-5:])

""" Modifying strings """

#UpperCase
a = "David"
print(a.upper())
#lowercase
print(a.lower())

# rm whitespace from start and end
a = "    David      "
print(a.strip())

# replace string sequences with others
a = "1234512"
print(a.replace("12", "ab"))
# This happens for all occurences, not just the first one

# Split into a list
a = "Hello, World!"
print(a.split(","))

# string concatenation
b = a + " :)"
print(b)

""" F strings... think formatting """

myPrice = 5.9912
offer = f"The price for the day is {myPrice}"
print(offer)

# Modifiers
offer = f"The price for the day is {myPrice:.2f}"
print(offer)
print(f"For 7 days, this equates to: {myPrice * 7:.2f}")

""" Escape chars """

# a backslash can be used to represent characters that may cause issues
txt = "The top of the \" mountain \""
print(txt)

""" More escape characters:

    Remember to not have a space between the backslash and associated char
    \ '	Single Quote	
    \ \	Backslash	
    \ n	New Line	
    \ r	Carriage Return	
    \ t	Tab	
    \ b	Backspace	
    \ f	Form Feed	
    \ ooo	Octal value	
    \ xhh	Hex value

 """

""" String methods:

    capitalize()	Converts the first character to upper case
    casefold()	    Converts string into lower case
    center()	    Returns a centered string
    count()	        Returns the number of times a specified value occurs in a string
    encode()	    Returns an encoded version of the string
    endswith()	    Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	        Searches the string for a specified value and returns the position of where it was found
    format()	    Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	        Searches the string for a specified value and returns the position of where it was found
    isalnum()	    Returns True if all characters in the string are alphanumeric
    isalpha()	    Returns True if all characters in the string are in the alphabet
    isascii()	    Returns True if all characters in the string are ascii characters
    isdecimal()	    Returns True if all characters in the string are decimals
    isdigit()	    Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	    Returns True if all characters in the string are lower case
    isnumeric()	    Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	    Returns True if all characters in the string are whitespaces
    istitle()	    Returns True if the string follows the rules of a title
    isupper()	    Returns True if all characters in the string are upper case
    join()	        Joins the elements of an iterable to the end of the string
    ljust()	        Returns a left justified version of the string
    lower()	        Converts a string into lower case
    lstrip()	    Returns a left trim version of the string
    maketrans()	    Returns a translation table to be used in translations
    partition() 	Returns a tuple where the string is parted into three parts
    replace()	    Returns a string where a specified value is replaced with a specified value
    rfind()	        Searches the string for a specified value and returns the last position of where it was found
    rindex()	    Searches the string for a specified value and returns the last position of where it was found
    rjust()	        Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	    Splits the string at the specified separator, and returns a list
    rstrip()	    Returns a right trim version of the string
    split()	        Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	        Returns a trimmed version of the string
    swapcase()	    Swaps cases, lower case becomes upper case and vice versa
    title()	        Converts the first character of each word to upper case
    translate()	    Returns a translated string
    upper()	        Converts a string into upper case
    zfill()	        Fills the string with a specified number of 0 values at the beginning

 """

""" Boolean expressions """

print(10>9) # true
print(1 == 1) # true
print(2 != 2) # false

# in action
a = 1
b = 2
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

# What happens when we cast to a bool then?
print(bool(12))
print(bool(""))
print(bool("hello"))
print(bool(None))
print(bool())
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))
# So it looks like, so long as it is not blank or nothing at all... then it equates to true... it just checks if there is content.
# Could be useful when checking if the user has entered something?

a= ""
if a:
    print(bool(a))
else:
    print("damn")

# So it is checking if a = true... but a is empty so this equals false... Thus is jumps to the else clause instead........... Check out the below
if not a:
    print(bool(a))
else:
    print("damn")

# defined subroutines can also act as functions
def myFunction():
    return True

if myFunction():
    print("Yes")
else:
    print("No")

""" Operators:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

    ARITHMATIC
    +	Addition	x + y	
    -	Subtraction	x - y	
    *	Multiplication	x * y	
    /	Division	x / y	
    %	Modulus	x % y	
    **	Exponentiation	x ** y	
    //	Floor division	x // y

    ASSIGNMENT
    =	x = 5	x = 5	
    +=	x += 3	x = x + 3	
    -=	x -= 3	x = x - 3	
    *=	x *= 3	x = x * 3	
    /=	x /= 3	x = x / 3	
    %=	x %= 3	x = x % 3	
    //=	x //= 3	x = x // 3	
    **=	x **= 3	x = x ** 3	
    &=	x &= 3	x = x & 3	
    |=	x |= 3	x = x | 3	
    ^=	x ^= 3	x = x ^ 3	
    >>=	x >>= 3	x = x >> 3	
    <<=	x <<= 3	x = x << 3	
    :=	print(x := 3)	x = 3
    print(x)

    COMPARISON
    ==	Equal	x == y	
    !=	Not equal	x != y	
    >	Greater than	x > y	
    <	Less than	x < y	
    >=	Greater than or equal to	x >= y	
    <=	Less than or equal to	x <= y

    LOGICAL
    and 	Returns True if both statements are true	x < 5 and  x < 10	
    or	Returns True if one of the statements is true	x < 5 or x < 4	
    not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

    IDENTITY
    is 	Returns True if both variables are the same object	x is y	
    is not	Returns True if both variables are not the same object	x is not y

    MEMBERSHIP
    in 	Returns True if a sequence with the specified value is present in the object	x in y	
    not in	Returns True if a sequence with the specified value is not present in the object	x not in y

    BITWISE
    & 	AND	Sets each bit to 1 if both bits are 1	x & y	
    |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
    ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
    ~	NOT	Inverts all the bits	~x	
    <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
    >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
 """

""" Precedence in order >>> Get used to using parenthesis to specify order 

    ()	Parentheses	
    **	Exponentiation	
    +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
    *  /  //  %	Multiplication, division, floor division, and modulus	
    +  -	Addition and subtraction	
    <<  >>	Bitwise left and right shifts	
    &	Bitwise AND	
    ^	Bitwise XOR	
    |	Bitwise OR	
    ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
    not	Logical NOT	
    and	AND	
    or	OR

    If two operators have the same precedence then it is from left to right.
"""

""" Lists """

# used to store many items in one variable
mylist = ["abc", 10, 'c']
# Looks like you can have a list containing different data types
# checking
print(type( mylist[0]))
print(type( mylist[1]))
print(type( mylist[2]))
# correct. I do not like it.

# list is changeable, meaning we can add remove and change items after they have been created.
mylist[0] = 5
print(mylist)

# lists allow for duplicates
mylist.append(10)
print(mylist)

mylist.reverse()
print(mylist)

# len works for lists too! Not just strings
print(len(mylist))

## Lists are predefined objects with the data type of a 'list'

# Constructing a list
newList = list(("a", "b", "d", "c", "a"))
print(newList)

""" 
    List: ordered and changeable colleciton :: Allows duplicate elements
    Tuple: ordered but unchangeable collection :: Allows duplicate elements
    Set: UNordered and UNchangeable collection :: NO duplicate elements ::: NOTE: NOT INDEXED
    Dictionary: ordered and unchangeable collection :: NO duplicate elements
        NOTE >> Py 3.6 and earlier they were unordered
 """

## Todo: reached this point
## https://www.w3schools.com/python/python_lists_access.asp
## (Python lists > Access list items)