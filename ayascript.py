import ayarandom

def pastTense(word):
    return

def anA(word):
    if word[0].lower() in "aeio":
        return "an "+word
    else:
        return "a "+word

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

def addModifier(word, mod):
    if mod == "a":
        return anA(word)
    if mod == "cap":
        return word.capitalize()
    if mod == "ed":
        return pastTense(word)
    if mod == "ing":
        return ing(word)


def getRandomItem(node, input):
    if "." not in node:
        if node not in input:
            raise Exception("Node error - node \"" + node + "\" not found")
        opts = [x for x in input[node]]
        return ayarandom.choice(opts)
    else:
        word = node.split(".")[0]
        modifier = node.split(".")[1]
        if word not in input:
            raise Exception("Node error - node \"" + node + "\" not found")
        opts = [x for x in input[word]]
        return addModifier(ayarandom.choice(opts), modifier)

def ayascript(input):
    if "output" not in input:
        raise Exception("Input error - origin not found")
    opts = [x for x in input["output"]]

    originToUse = ayarandom.choice(opts)
    output = ""
    hashedword = ""

    foundhash = False
    for letter in originToUse:
        if letter != "#" and not foundhash:
            output += letter
        elif letter == "#":
            foundhash = not foundhash
            if not foundhash:
                hashedword += "#"

                hashedword = getRandomItem(hashedword.replace("#", ""), input)

            output += hashedword
            hashedword = ""
        if foundhash:
            hashedword += letter

    return output