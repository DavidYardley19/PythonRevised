from openai import OpenAI
#client = OpenAI(api_key="")
# Remove the comment above and add your API key to use the code below

plot = input("What would you like the plot of the story to be: ")
genre = input("What would you like the genre of the story to be: ")
endingType = input("What would you like the ending of the story to be like: ")
storyLength = input("How long would you like the story to be: ")
print()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"Make me a {storyLength} story containing the plot: {plot}, genre: {genre}, and ending type: {endingType}."}
  ]
)

print(response.choices[0].message.content)
print()
