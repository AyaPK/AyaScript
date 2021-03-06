import json

def pastTense(word):
    with open("irregVerbs.json", "r") as f:
        irregulars = json.load(f)
    if word in irregulars:
        return irregulars[word]
    return word+"ed"

def anA(word):
    if word[0].lower() in "aeio":
        return "an " + word
    else:
        return "a " + word


def ing(word):
    if word[-1] in "dgnpm" and word[-2] in "aeiou":
        if word[-3] in "aeiou":
            return word + "ing"
        else:
            return word + word[-1] + "ing"
    elif word[-1] == "e":
        return word[0:-1] + "ing"
    else:
        return word + "ing"

def plural(word):
    return word+"s"