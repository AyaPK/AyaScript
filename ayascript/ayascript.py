from ayascript import ayarandom, ayaBrainFuck, ayagrammar


def randomDigit(lowest, highest):
    return ayarandom.number(lowest, highest)
def randomChoice(list):
    return ayarandom.choice(list)


def addModifier(word, mod):
    if mod == "a":
        return ayagrammar.anA(word)
    if mod == "cap":
        return word.capitalize()
    if mod == "low":
        return word.lower()
    if mod == "ed":
        return ayagrammar.pastTense(word)
    if mod == "ing":
        return ayagrammar.ing(word)
    if mod == "s":
        return ayagrammar.plural(word)


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


def ayagen(input):
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

def brainfuck(input):
    return ayaBrainFuck.brainfuck_transpiler(input)


def pseudocode(filePath):
    debug = False
    indentLevel = 0
    operators = "+-/*"
    execute = ""
    with open(filePath, "r") as file:
        lines = file.readlines()
    variables = {}
    for line in lines:
        if "//" in line.split(" ")[0]:
            continue
        elif "->" in line:
            newline = line.replace("->", "=")
            execute += "\t"*indentLevel + f"{newline}"
        elif line.split(" ")[0].lower() == "show":
            execute += "\t"*indentLevel + f"print({line.replace('show', '').strip()})\n"
        elif line.split(" ")[0] == "for":
            loopcount = line.split(" ")[1]
            execute += "\t"*indentLevel + f"for __loopcounter__ in range({loopcount}):\n"
            indentLevel += 1
        elif line.split(" ")[0] == "end\n":
            indentLevel -= 1
        elif line.split(" ")[0] == "if":
            line = line.replace("is", "==").replace("\n", "")
            execute += "\t" * indentLevel + line + ":" + "\n"
            indentLevel += 1
        elif line.split(" ")[0:2] == ["else", "if"]:
            line = line.replace("is", "==").replace("\n", "").replace("else if", "elif")
            execute += "\t" * indentLevel + line + ":" + "\n"
            indentLevel += 1
        elif line.split(" ")[0] == "else\n":
            line = line.replace("is", "==").replace("\n", "")
            execute += "\t" * indentLevel + line + ":" + "\n"
            indentLevel += 1
    if debug:
        print(execute)
    else:
        exec(execute)