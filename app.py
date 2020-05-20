import json

data = json.load(open('data.json'))

def lookup(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    else:
        return "The word doesn't exist! Please check the spelling."

user_input = input('Enter a word to lookup the dictionary: ')

print(lookup(user_input))