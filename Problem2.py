fruit_list = ['Apple', 'Orange', 'Pineapple', 'Banana', 'Strawberries']

# Part 2
print(f"The second item in the list is: {fruit_list[1]}")

# 3. print first 3 itmes
print(f"The first 3 items in the list are: {fruit_list[:3]}")

# 4. store fruit and prices in a dictionary called "fuit_dictionary" with the names of the fruit as keys and prices as values
fruit_dictionary = {
    'Apple': 0.50,
    'Orange': 0.39,
    'Pineapple': 1.00,
    'Banana': 0.29,
    'Strawberries': 1.50
}

# 5. print price of pineapple
print(f"The price of a pineapple is: {fruit_dictionary['Pineapple']}")

# 6. iterate through dictionary using .keys() method, print each fruit name along with price
for fruit in fruit_dictionary.keys():
    print(f"The price of {fruit} is: {fruit_dictionary[fruit]:.2f}")

# 7. change price of an apple to .55 in the dictionary
fruit_dictionary['Apple'] = 0.55

# 8. Due to inflation, all prices increase by 12%. Iterate through and update prices to reflect inflation
for fruit in fruit_dictionary.keys():
    fruit_dictionary[fruit] = fruit_dictionary[fruit] * 1.12

print()
for fruit in fruit_dictionary.keys():
    print(f"The price of {fruit} is: {fruit_dictionary[fruit]:.2f}")