import re


def encode(text):
    string = text
    string = list(string)
    result = []
    while string:
        letter = string[0]
        pattern = fr"\b{letter}+"
        cut = re.findall(pattern, ''.join(string))
        if len(*cut) == 1:
            result.append(letter)
        else:
            result.append(letter + str(len(*cut)))
        string = string[len(*cut):]
    return "".join(result)

