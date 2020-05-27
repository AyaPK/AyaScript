import ayarandom
import ayagrammar


def addModifier(word, mod):
    if mod == "a":
        return ayagrammar.anA(word)
    if mod == "cap":
        return word.capitalize()
    if mod == "ed":
        return ayagrammar.pastTense(word)
    if mod == "ing":
        return ayagrammar.ing(word)


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
