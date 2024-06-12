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

""" Python exercises provided by pictureFrame AI """



""" 
Task 1
Write a program that takes a list of integers as input and returns the sum of all the even
numbers in the list.
Example input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Example output: 30

 """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumOfList = 0
for i in range(0,len(list1) + 1, 2):
    sumOfList += i
print(f"The sum of the elements in the list: {list1} is equal to {sumOfList}")

""" 
Task 2
Write a program that takes a string as input and returns a new string that contains only
the first and last characters of the input string.
Example input: "hello"
Example output: "ho"

 """

exampleInput = input("Please enter a string, I will output the first and last character: ")
print(exampleInput[0]+exampleInput[-1])

""" 
Task 3
Write a program that takes two lists of integers as input and returns a new list that
contains only the common elements between the two lists (i.e., the elements that are
present in both lists).
Example input: [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7]
Example output: [3, 4, 5]

 """

inputOne = input("Please enter a list of integers seperated by spaces")
listOne = inputOne.split(" ")
listOneAsInt = []
for i in listOne:
    listOneAsInt.append(int(i))
set1 = set(listOneAsInt)

inputTwo = input("Please enter another list of integers seperated by spaces")
listTwo = inputTwo.split(" ")
listTwoAsInt = []
for i in listTwo:
    listTwoAsInt.append(int(i))
set2 = set(listTwoAsInt)

print("I will check for common elements in both")
set3 = set1.intersection(set2)
intersectionList = list(set3)
print(intersectionList)

## This is horribly conveluted.

""" 
Task 4
Write a program that takes a list of integers as input and returns a new list that contains
only the numbers that are greater than the average of all the numbers in the input list.

Example input: [10, 20, 30, 40, 50]
Example output: [40, 50]

In the above example, the average of the input list is 30, so the program should return a
new list containing only the numbers that are greater than 30, which are 40 and 50.
"""

input1 = input("Please enter a list of integers, seperated by spaces: ")
list1_String = input1.split(" ")
list1_int = []
for c in list1_String:
    list1_int.append(int(c))
sumOfList = sum(list1_int)
averageOfList = sumOfList / len(list1_int)
intAboveAverage = []
for c in list1_int:
    if c > averageOfList:
        intAboveAverage.append(c)
print(f"All values above the average = {intAboveAverage}")


""" 
Task 5
Write a program that takes a string as input and returns a new string that is the reverse
of the input string. For example, if the input string is "hello", the program should return
"olleh".
Example input: "hello"
Example output: "olleh"
"""

myString = "david"
reversedString = ""
for i in range(len(myString) -1, -1, -1):
    reversedString += myString[i]
print(reversedString)
# There is a more sleek version
reversedString = myString[::-1]
print(reversedString)

"""
Task 6
Write a program that takes a list of integers as input and returns a new list that contains
only the positive even numbers in the input list.

Example input: [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
Example output: [2, 4, 6]

In the above example, the program should first filter out all the negative integers, then
only select the even numbers, which are 2, 4, and 6.

"""

rawList = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
positiveEvenList = []
for i in rawList:
    if i%2==0 and i>=0:
        positiveEvenList.append(i)
print(positiveEvenList)

"""
Task 7
Write a program that takes a positive integer as input and prints out the multiplication
table for that integer up to 10.

Example input: 5
"""

userInput = int(input("Please enter an integer: "))
for i in range(1,11):
    print(f"{i} x {userInput} = {i*userInput}")