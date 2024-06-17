

"""
In this problem we will use Python to assign values to variables in order to perform calculations on these variables

The challenge is to write a program that calculates the total cost of a purchase, including tax and a discount

There are three products purchased with the following prices:
Trousers: £20
Shirt: £15.99
Shoes: £29.99

The tax rate and discount rate are as follows:
Tax: 8%
Discount: 20%

--

Print data type of each var
Calculate total cost of purchase... after tax and discount applied.
Customer wants to returns 2 shoes and 3 trousers - purchased with discount and tax rates.
    > They want to buy as many shirts with the money they get back. Calculate money left over after buying max shirts

"""

tax_rate = 0.08
discount_rate = 0.20
trousers = 20
shirt = 15.99
shoes = 29.99

number_of_shoes = 0
number_of_trousers = 0
number_of_shirts = 0

def Show_Data_Type():
    print("Data type of trousers: ", type(trousers))
    print("Data type of shirt: ", type(shirt))
    print("Data type of shoes: ", type(shoes))
    print("Data type of tax_rate: ", type(tax_rate))
    print("Data type of discount_rate: ", type(discount_rate))

Show_Data_Type()

number_of_shoes = int(input("How many shoes would you like to purchase: "))
number_of_shirts = int(input("How many shirts would you like to purchase: "))
number_of_trousers = int(input("How many trousers would you like to purchase: "))


def Calculate_Total_Cost():
    total_cost = ((trousers*number_of_trousers) + (shirt*number_of_shirts) + (shoes*number_of_shoes)) * (1-tax_rate) * (1-discount_rate)
    print("Total cost of purchase: £", total_cost.__format__(".2f"))

Calculate_Total_Cost()

def Calculate_Money_Left_Over():
    total_cost = ((shoes*2) + (trousers*3)) * (1-tax_rate) * (1-discount_rate)
    print(total_cost.__format__(".2f"))
    number_of_shirts = total_cost//shirt
    money_left_over = total_cost % shirt
    print("Number of shirts purchased: ", number_of_shirts)
    print("Money left over: £", money_left_over.__format__(".2f"))

Calculate_Money_Left_Over()