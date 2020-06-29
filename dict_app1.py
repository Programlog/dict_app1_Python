import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word].

    elif word.title() in data:
        return data[word.title()]

    elif len(get_close_matches(word, data.keys())) > 0:
        re_enter = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead?(Y/N) ")

        if re_enter.lower()[0] == 'y':
            return data[get_close_matches(word, data.keys())[0]]

        elif re_enter.lower()[0] == 'n':
            re_enter = input(f"Did you mean {get_close_matches(word, data.keys())[1]} instead?(Y/N) ")

            if re_enter.lower() == 'y':
                return data[get_close_matches(word, data.keys())[1]]

            elif re_enter.lower()[0] == 'n':
                re_enter = input(f"Did you mean {get_close_matches(word, data.keys())[2]} instead?(Y/N) ")

                if re_enter.lower() == 'y':
                    return data[get_close_matches(word, data.keys())[2]]

                elif re_enter.lower()[0] == 'n':
                    return "Sorry it looks like the word you entered is not in the dictionary"


            else:
                return "Sorry please type Y or N "

        else:
            return "Sorry please type Y or N "

    else:
        print("The word doesn't exist. Please double check your word ")


users_word = input("Enter a word: ")

output = translate(users_word)

if type(output) == list:
    print('\n'.join(output))

else:
    print(output)
