# Exercise 1
"""
Write a function that takes in a certain amount of integers as arguments and returns their sum.

For example, if the function is called add_numbers(2, 3), it should return 5. 
If the function is called add_numbers(2,3,4,5), it should return 14.
"""
def add_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    print("The sum of all the values =" , sum)

add_numbers(2,3)
    # Returns 5, YES
add_numbers(2,3,4,5)
    # Returns 14, YES

# Exercise 2
"""
Write a function that takes in a string and returns the string reversed. 

For example, if the function is called reverse_string('hello'), it should return 'olleh'.
"""
def reverse_string(myString):
    print(myString[::-1])

reverse_string("hello")
    # Returns 'olleh', YES


# Exercise 3
"""
Write a function that takes in a list of integers and returns the average of the numbers in the list.

For example, if the function is called calculate_average([1, 2, 3, 4, 5]), it should return 3.0.
"""
def calculate_average(numbers):
    print(sum(numbers)/len(numbers))

calculate_average([1,2,3,4,5])
    # Returns 3.0, YES


# Exercise 4
"""
Write a function that takes in a string and a character, and returns the number of times the character appears in the string. 

For example, if the function is called count_char('hello world', 'o'), it should return 2.
"""
def count_char(myString, myChar):
    print(myString.count(myChar))

count_char('hello world', 'o')
    # Returns 2, YES

# Exercise 5
"""
Write a function that takes in a list of integers and returns a new list that contains only the even numbers from the original list. 

For example, if the function is called get_even_numbers([1, 2, 3, 4, 5]), it should return [2, 4].
"""
def get_even_numbers(numbers):
    newList = []
    for i in numbers:
        if i%2==0:
            newList.append(i)
    print(f"The even numbers for this list is: {newList}")

get_even_numbers([1, 2, 3, 4, 5])
    # Returns [2,4], YES

# Exercise 6
"""
Write a function that takes in a list of strings and returns the longest string in the list. 

For example, if the function is called find_longest_string(['hello', 'world', 'python']), it should return 'python'.
"""
def wrong_find_longest_string(*args):
    longestString = args[0]
    if len(args) > 1:
        for i in range(1,len(args)):
            if len(args[i]) > len(longestString):
                longestString = args[i] 
    print("The longest string is:", longestString)
        
wrong_find_longest_string('hello', 'world', 'python')
# But that was not in the specification, the task specified for a LIST of strings... appending "wrong" to the start of the function
### PYTHON DOES NOT SUPPORT OVERLOADING, I DO NOT LIKE THIS.
    # Having the same function name but with a different signature would have been very nice.
def find_longest_string(stringList):
    longestString = stringList[0]
    if len(stringList) > 1:
        for i in range(1,len(stringList)):
            if len(stringList[i]) > len(longestString):
                longestString = stringList[i] 
    print("The longest string is:", longestString)

find_longest_string(["hello"])
find_longest_string(['hello', 'world', 'python'])
    # Returns 'python', YES

# Exercise 7
"""
Write a function that takes in a list of integers and returns the product of the numbers in the list.

For example, if the function is called calculate_product([1, 2, 3, 4, 5]), it should return 120.
"""
def calculate_product(numbers):
    product = 1
    for n in numbers:
        product*=n
    print(product)

calculate_product([1, 2, 3, 4, 5])
    # Returns 120, YES


# Exercise 8
"""
Write a function that takes in a string and a list of words, and returns the number of times each word appears in the string. 

For example, if the function is called count_words('hello world hello', ['hello', 'world']), it should return {'hello': 2, 'world': 1}.
"""
# Ooh, a dictionary? Need a quick check up on this
# TODO: Testing what happens when you cast a list into a dict
""" mylist = ["hello", "world"]
myDict = dict(mylist)
print(myDict) 
"""
# It does not like this
myList = ["hello", "world"]
myString = 'hello world hello'

def count_words(myString, myList):
    """
    Initialises a dictionary containing the strings in the list provided, each with a value of 0
    Iterates over the dictionary, checking how many occurences that key appears in the string provided.
    
    Output: Dictionary
    """
    # I think this is called comprehension. TODO: Check what this is referred to as in technical terms.
    myDict = {string: 0 for string in myList}
    for key in myDict:
        myDict[key] += myString.count(key)
    print(myDict)

count_words(myString, myList)
    # Returns: {'hello': 2, 'world': 1}, YES.

# A little practice with docstrings... Will make a habit of using these moving forward.
""" help(count_words) """
# Should probably look up what the best practice is industry-wide. TODO: Question: Does this relate to PEP-8?

# Exercise 9
"""
Write a function that takes in a list of strings and a string, and returns a new list that contains only the strings from the original list that contain the given string. 

For example, if the function is called find_strings(['hello', 'world', 'python'], 'l'), it should return ['hello', 'world'].
"""
# Note: I personally do not like using single quotes since there exists another language that specifically uses single quotes for characters... could be JAVA, will have to check
my_list = ['hello', 'world', 'python']
my_string = "l"
def find_strings(my_list, my_string):
    """
    Initialises an empty 'output' list.
    Iterates over the list of elements provided, checking if the string provided is contained within element.
    If it is contained within the element, this is added to the output list. 

    Output: Output list containing all elements of the input list which contain the string provided.
    """
    output_list = []
    # Well, I also do not like using string since I treat it as a keyword in my head. But I will amend this once I find a better practice.
    for element in my_list:
        if my_string in element:
            output_list.append(element)
    print(output_list)

find_strings(my_list, my_string)
    # Returns ['hello', 'world'], YES

# Exercise 10
"""
Write a function that takes in a list of integers and returns the maximum difference between any two numbers in the list. 

For example, if the function is called calculate_max_difference([1, 2, 3, 4, 5]), it should return 4.
"""
myList = [1, 2, 3, 4, 5]
def calculate_max_difference(myList):
    """ 
    Initialises the smallest and largest value to be equal to the first element (index 0) in the list provided.
    Iterates over the list from the next value (index 1) onwards. The program will check if this is less/greater than the initialised values and replaces accordingly.
    
    Output: largestValue - smallestValue
    """
    # An arbitrary value such as 0 cannot be set for smallest and largest since it might not be contained in the list, or lay somewhere in the middle of the list
    smallestVal = myList[0]
    largestVal = myList[0]
    if len(myList) > 1:
        for val in range(1, len(myList)):
            if myList[val]<smallestVal:
                smallestVal = myList[val]
            elif myList[val]>largestVal:
                largestVal = myList[val]
        print(largestVal-smallestVal)
    else:
        print(1)

calculate_max_difference(myList)
    # Returns 4, YES