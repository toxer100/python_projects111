import json
from difflib import get_close_matches

data = json.load(open("files/data.json"))

def translate(w):
    w = w.lower()
    get_close = get_close_matches(w, data.keys(), n = 5)
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close) > 0 and w != "/end":
        for i in range(0, len(get_close)):

            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close[i])
            if yn == "Y":
                return data[get_close[i]]
            elif yn == "N":
                print("Ok, there is another variant.")
                continue 
                
            else:
                print("We didn't understand your entry./n Try another variant")
                continue 
                
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

str1 = "Enter word: "

while True:
    
    word = input(str1)
    str1 = "Enter another word: "
    output = translate(word)
    if word == "/end":
        break
    elif type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)