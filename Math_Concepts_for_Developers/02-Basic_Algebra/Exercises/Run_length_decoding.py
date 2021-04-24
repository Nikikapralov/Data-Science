import re

def decode(text):
    string = text
    pattern_letters = fr'\b[A-Z]'
    pattern_digits = fr'\b[0-9]+'
    string = list(string)
    result = ''
    while string:
        letter = re.findall(pattern_letters, ''.join(string))[0]
        string = string[len(letter):]
        amount = re.findall(pattern_digits, ''.join(string))
        if not amount:
            result += letter
            continue
        else:
            result += letter * int(amount[0])
            string = string[len(amount[0]):]
    return result
