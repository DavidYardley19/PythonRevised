def ReturnProduct(a,b):
    return a*b

def ReturnSumOfFirstAndFourth(list):
    return list[0] + list[3]

import math
def CalcCircleArea(radius):
    return math.PI * radius**2

def multiplyLists(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum += list1[i] * list2[i]

def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False
    