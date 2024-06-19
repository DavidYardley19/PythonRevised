from datetime import date

"""
Plan:
    1. Utilise OpenAi API to generate blog content


"""

subject = input("What is the subject of your blog post: ")
length = input("How long would you like the blog post to be: ")
writingStyle = input("What style of writing would you like to use: ")
today = date.today()
today_string = today.strftime("%B %d, %Y")

print("Today's date is:", today_string)