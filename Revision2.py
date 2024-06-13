# starting point: https://www.w3schools.com/python/python_lists_access.asp

""" Plan to do an hour and a half of this then move on to the next topic - probably cloud... Infact, I'll listen to some cloud videos/ podcasts whilst doing this. Then full focus
    Probably not most efficient for learning but I'm young - now is the time to * around and find out.
 """

myList = [1,2,3,4,"David", True]
print(myList[1])
# This will output 2, since indexing starts from 0

#negative indexing
print(myList[-1])
# this refers to the last item

# range of indexes
print(myList[1:3])
# prints the 1st, and 2nd index since it works as [a,b] = a, a+1, a+2, ..., b-1

# from start to n, or n to end
print(myList[:3])
print(myList[3:])

""" Check if the item exists in a collection """
if 3 in myList:
    print("3 is in the list")
elif 4 in myList:
    print("3 is not in the list, but 4 is")
else:
    print("Neither 3 or 4 is in the list")

# This can also be done with strings
myString = "David Charlie Adam Sam"
if "David" in myString:
    print("David is in the string")

""" Remember, lists are mutable... they can be added removed and changed """
myList = [5,4,3,2,1]
print(myList)
myList[0] = 0
print(myList)
myList[0:3] = [99, 98]
print(myList)

""" You can insert more items than you replace! I would be very careful with this """
newList = [1,2,3]
newList[1:2] = [4,5,6,7,8,9]
print(newList)
# So here changed the one val at index_1 to [4,5,6,7,8,9]

""" The same works for reducing multiple vals into just the one """
anotherList = [1,2,3,4,5]
anotherList[1:3] = [99]
print(anotherList)

#
""" Insert at a specific location without affecting other items """
insertList = [0,1,2,3,4]
insertList.insert(2, 99)
print(insertList)
# This inserts the value 99 into the second index without affecting the first values in the list, everything else gets moved down one. 

""" Adding an item to the end of the list """
# Test: Can this also be done with insert so long as you are using -1 as the index, or will it just move the last value to the right once again
insertList.insert(-1, 77)
print(insertList)
# ANSWER: it does just move the last value right one, so it is best to use append when adding to the end. Think of a stack or queue
insertList.append(77)

###
"""
            TODO
                    Need to check on the below, set a breakpoint and investigate on why it is doing this.
            TODO
"""
###

""" Append all the elements from another list """
firstList = ["a", "b", "c"]
secondList = [1,2,3]
joinedList = firstList.extend(secondList)
print(joinedList)
# Now why is it that this list is completely empty? >> OUTPUT: None
joinedList = firstList + secondList
print(joinedList)
# I do not understand any of this! >> OUTPUT: ['a', 'b', 'c', 1, 2, 3, 1, 2, 3]

# Just going to do it the simplified way.

firstList.extend(secondList)
print(secondList)
# Now the output is different... OUTPUT: [1, 2, 3]

## The extend will also append other iterable objects such as tuples sets dictionaries etc.

""" Remove will remove a specified item... but only the first occurence. """
# I wonder, will there be an error if I try to remove an item that is not there?
myList = [1,2,3]
## myList.remove(4)
# Yes there will be an error.

""" pop() can be used to remove the last item, but it can also be used to remove at a specific location if you give it an index val 
    del keyword does the  same thing
"""
myList = [1,2,3,4]
print(myList)
myList.pop()
print(myList)

myList.pop(0)
print(myList)
del myList[1]
print(myList)

""" The clear() method empties the list but leaves the list object alone """
myList.clear()
print(myList)

""" Looping through a list """
numbers = [1,4,2,88,3]

for x in numbers:
    print(x)
print()

for y in range(len(numbers)):
    print(numbers[y])
print()

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
print()

# Learn how to use list comprehension
# https://www.w3schools.com/python/python_lists_loop.asp

""" 
dt. 13/06/2024
LetsGetIt
"""

# List comprehension
thisList = ["apple", "banana", "cherry"]
print((x) for x in thisList)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []
for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)

# This can all be done in one line!! Need to check over the exercises given last session!¬!
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x!= "kiwi"]
print(newlist)

# Note that the conditional is optional
newlist = [x for x in fruits]

# Range function can be used here
evenNumbers = [x for x in range(0,21,2)]
print(evenNumbers)

# String manipulation can be used!

upperFruits = [x.upper for x in fruits]
print(upperFruits)

# using else
print(fruits)
newlist = [x if x!= "banana" else "orange" for x in fruits]
print(newlist)

""" Sorting lists """

# .sort >> ALphanumeric asc by def
print(f"Fruits unsorted, then sorted")
fruits.append("blueberry")
print(fruits)
fruits.sort()
print(fruits)

# Test: do capitals come first?
fruits.append("ZuluFruit")
fruits.sort()
print(fruits)
# Answer: Yes, yes they do >> Maybe it runs on order of ascii, or unicode?

myNumbers = [1,2,3,4,1]
myNumbers.sort()
print(myNumbers)

# Sorting by reversed
myNumbers.sort(reverse=True)
print(myNumbers)

# Customising the sort function using "key = function"
def myfunc(n):
    return abs(n-50)

thisList = [100,182,0,23]
thisList.sort(key = myfunc)
print(thisList)
# It does not look right?
# No it is right, it sorts it by how close each value is to 50, but retains the initial values... Interesting.
    # Back end of back end programming lol

# Tackling case sensetive shorting
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Capitals come first here
thislist.sort(key = str.lower)
print(thislist)

""" Copying lists
NOTE: be very careful when doing list1 = list2 ... because they are simply just references to a list collection... any changes done in list2 are also made in list1

use list.copy()
 """

thislist = [1,2,4]
copiedList = thislist.copy()
print(copiedList)

# Another way using the constructor method: list()
copiedList2 = list(thisList)
print(copiedList2)

""" Joining two lists """
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
list1plus2 = list1 + list2
print(list1plus2)
# Seems like the same as just extending the list?

# Keeping list 1 but appending each element in list 2
for x in list2:
    list1.append(x)
print(list1)

# Extending as mentioned before:
list1 = [1,2,3]
list1.extend(list2)
print(list1)

""" 
List methods:
    append()	Adds an element at the end of the list
    clear() 	Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list

    All have been done.
"""

#
"""  """
#

""" 
Going to work on some tuples before checking out API's

Ordered, immutable
Written with (rounded brackets)
Alows duplicates
"""

myTuple = (1,2,3,4,4,4)
print(myTuple , "has a length of:" , len(myTuple))

# You can have a tuple with just one value
singleVal = (1,)
print(type(singleVal))
# Typically a good idea to just add a comma after the values anyway
goodTuple = (1,2,3,4,)
print(type(goodTuple))
# You cannot have the following, the brackets do nothing here
singleVal = (1)
print(type(singleVal))

""" Tuples can contain different data types """
mixedTuple = (1,2.222,True, "Hello",)

""" tuple constructor can be used to create a tuple, I wonder if you can inset a list and a set here? """
mySet = {1,2,3}
myList = [1,2,3]
myTuple = tuple(mySet)
myTuple = tuple(myList)
# Yes you can
# Inserting vals directly, you need two parenthesis
myTuple = tuple((1,2,3,4,5))
print(myTuple)

""" Accessing items, indexing can be used with the squared brackets """
print(myTuple[0])
# The first value in the tuple is outputted
# Negative indexing can be used all the same

# Checking if the tuple contains a specific element
if 2 in myTuple:
    print("2 is in tuple")

""" Updating tuples... they are immutable, but there is a workaround... change it to a list then back to a tuple """
x = (1,2,3)
y = list(x)
y[0] = 99
y.append(0)
x = tuple(y)
print(x)

""" Adding two tuples """
z = (44,)
x += z
print(x)

""" del can be used to remove a tuple """
del x
# print(x) >> Will not work since it is gone

""" Unpacking a tuple """

# Example of packing
numbers = (255,0,122,)
# Extract values back into variables, this is unpacking
(r,g,b) = numbers
print(r)
print(g)
print(b)

""" Using an * :: if num of vars is less than the number of vals, * can be used """
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# TODO: Question, what if you put it in the middle
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
# So python is able to recognise that you have 1-1 var-val relations on the end

# TODO: Question, what if you have two asterisks?
""" (green, *yellow, *red) = fruits

print(green)
print(yellow)
print(red) 

# This produces an error
"""

""" Looping """
myTuple = (10,20,30,)
for x in myTuple:
    print(x)

for i in range(len(myTuple)):
    print(myTuple[i])

# Using a while loop >> Less of a fan with this one since more checks need to be made
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i += 1

""" Multiplying tuples """
fruits = ("apple", "banana", "cherry")
mult = 2
myTuple = fruits * mult
print(myTuple)
# Just seems like extending the tuple by mult times.

""" Methods:
    count()	Returns the number of times a specified value occurs in a tuple
    index()	Searches the tuple for a specified value and returns the position of where it was found
        >>> I believe this only does it for the first instance
 """

# checking index
numbers = (1,2,3,1,)
print(numbers.index(1))
# Obviously you "cant" find the index of an item which isnt in the collection 

""" 
moving on to sets

Written with curly braces

They are unordered, unindexed and immutable***
    *** >> You can remove and add new items... BUT CANNOT CHANGE ITEMS

NOTE: YOU CAN NOT HAVE DUPLICATE VALUES IN SETS   
"""

mySet = {1,2,3,4,5,"hello", False, 1.23456}
# Note this isssss fine.... But be very careful
    # True = 1
    # False = 0
# Since you cant have dupes, be VERY careful.

# So what if we have a set with both?
dupeSet = {False, 0, True, 1}
print(dupeSet)
dupeSet = {0, False, 1, True}
print(dupeSet)
# So you can add elements, but if it already exists in the set Left-To-Right... Then the computer 'ignores' the ones added. Length doesnt change

# Length
print(len(mySet))
print(type(mySet))

# Set constructor:
newSet = set((1,2,3,4,5,6,7))
print(newSet)
# Double rounded brackets again

# Can you pass it a list?
newlist = [1,2,3,4,5,5,5,5,5]
    # 5,5,5,5,5... added to check the no dupe feature
newSet = set(newlist)
print(newSet)

""" Accessing items """
for x in mySet:
    print(x)

print(mySet)
# Check for ownership
print(2 in mySet)
# Check for not- ownership
print(1 not in mySet)

""" Adding set items """
# jsut like append, but instead you use add
mySet = {1,2,3}
mySet.add(4)
print(mySet)

# to add items from another set:
addingSet = {7,8,9}
mySet.update(addingSet)
print(mySet)

# TODO: Can you use comprehension to add a list of items?
mySet = {1,2,3}
mySet.update(x for x in range(10) if x%2==0)
print(mySet)

## Up to : Adding any iterable
## https://www.w3schools.com/python/python_sets_add.asp