def removeDeadCommand(inp):
    notFound = True
    while notFound:
        inp = "".join(x for x in inp if x in "+-<>,.[]")
        if "+-" in inp or "<>" in inp or "[]" in inp or "-+" in inp or "><" in inp:
            inp = inp.replace("+-", "")
            inp = inp.replace("<>", "")
            inp = inp.replace("[]", "")
            inp = inp.replace("-+", "")
            inp = inp.replace("><", "")
            continue
        notFound = False
    return inp

def plus(count):
    return f"m[p] += {count}\n"

def min(count):
    return f"m[p] -= {count}\n"

def yplus(count):
    return f"p += {count}\n"

def ymin(count):
    return f"p -= {count}\n"

def brainfuck_transpiler(source_code):
    prepend = "m = [0]*30000\n" \
             "p = 0\n" \
             "output = \"\"\n" \
             ""
    output = ""

    indent = 0
    pointer = 0
    source_code = removeDeadCommand(source_code)
    inif = 0
    if source_code.count("[") != source_code.count("]"):
        raise Exception("Unexpected EOF while parsing. Loop not closed.")
    while True:
        if pointer == len(source_code):
            break

        if source_code[pointer] == "+":
            pluscounter = 0
            try:
                while source_code[pointer] == "+":
                    pluscounter += 1
                    pointer += 1
            except:
                pass
            output = output+(" ")*indent+plus(pluscounter)

        elif source_code[pointer] == "-":
            mincounter = 0
            try:
                while source_code[pointer] == "-":
                    mincounter += 1
                    pointer += 1
            except:
                pass
            output = output+(" ")*indent+min(mincounter)

        elif source_code[pointer] == ">":
            mincounter = 0
            try:
                while source_code[pointer] == ">":
                    mincounter += 1
                    pointer += 1
            except:
                pass
            output = output+(" ")*indent+yplus(mincounter)

        elif source_code[pointer] == "<":
            mincounter = 0
            try:
                while source_code[pointer] == "<":
                    mincounter += 1
                    pointer += 1
            except:
                pass
            output = output+(" ")*indent+ymin(mincounter)

        elif source_code[pointer] == ".":
            output = output+(" ")*indent+"output+=(chr(m[p]))\n"
            pointer += 1

        elif source_code[pointer] == ",":
            output = output+(" ")*indent+"c = input(\"> \")\n"+(" ")*indent+"if c == \"-1\":\n"+(" ")*indent+"    m[p] = -1\n"+(" ")*indent+"else:\n"+(" ")*indent+"    m[p] = ord(c)\n"
            pointer += 1

        elif source_code[pointer] == "[":
            inif += 1
            if "]" not in source_code[pointer:]:
                raise Exception("Unexpected EOF while parsing. Loop not closed.")
            output = output+(" ")*indent+"while m[p] > 0:\n"
            indent += 4
            pointer += 1

        elif source_code[pointer] == "]":
            if inif == 0:
                raise Exception("Syntax error, attempting to close non existent loop.")
            indent -= 4
            pointer += 1
            inif -= 1

        else:
            pointer += 1

    exec(prepend+output+"print(output)")

    return output

def rot13(input):
    rot13 = """-,+[-[>>++++[>++++++++<-]<+<-[>+>+>-[>>>]<[[>+<-]>>+>]<<<<<-]]>>>[-]+>--[-[<->+++[-]]]<[++++++++++++<[>-[>+>>
    ]>[+[<+>-]>+>>]<<<<<-]>>[<+>-]>[-[-<<[-]>>]<<[<<->>-]>>]<<[<<+>>-]]<[-]<.[-]<-,+]"""