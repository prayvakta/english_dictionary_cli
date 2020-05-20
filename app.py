import json
from difflib import SequenceMatcher

data = json.load(open('data.json'))

def match(word):
    matched_word = []
    for w in data.keys():
        if SequenceMatcher(None, w, word).ratio() > 0.8:
            matched_word.append(w)
    return matched_word

def lookup(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    else:
        matched_words = match(word)
        if len(matched_words) > 0:
            print('Did you mean any of these words?')
            return matched_words
        else:
            return "The word doesn't exist! Please check the spelling."

user_input = input('Enter a word to lookup the dictionary: ')

print(lookup(user_input))