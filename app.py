import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def match(word):
    return get_close_matches(word, data.keys(), 1)

def recommend_word(unmatched_word):
    matched_word = match(unmatched_word)
    if len(matched_word) > 0:
        user_confirm = input('Did you mean {!r}? Please press "Y" to confirm or "N" to enter a different word: '.format(matched_word[0]))
        if user_confirm.upper() == 'Y':
            return data[matched_word[0]]
        elif user_confirm.upper() == 'N':
            user_new_word = input('Enter another word: ')
            return(lookup(user_new_word))
        else:
            return ('Sorry, unrecognized input!!')
    else:
        return "The word doesn't exist! Please check the spelling."

def lookup(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    else:
        return recommend_word(word)

user_input = input('Enter a word to lookup the dictionary: ')

print(lookup(user_input))
