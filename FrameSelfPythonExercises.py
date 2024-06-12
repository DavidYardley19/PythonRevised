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